"""
analyze_data.py - Flight Simulator Training Data Analysis
===========================================================

Purpose:
  Analyze flight simulator training data using pandas groupby operations.
  Distinguishes between:
  - STUDENTS (who take training)
  - SESSIONS (individual training events)
  
  Provides comprehensive analysis across multiple dimensions:
  - Student performance and pass rates
  - Session characteristics (type, difficulty, date)
  - Instructor workload and effectiveness
  - Simulator utilization
  - Exercise type performance

Usage:
  python scripts/analyze_data.py

Expected Output:
  - SECTION 1: STUDENTS SUMMARY (groupby student_id)
  - SECTION 2: FLIGHT SESSIONS SUMMARY (groupby date, type, difficulty)
  - SECTION 3: INSTRUCTOR WORKLOAD (groupby instructor_id)
  - SECTION 4: SIMULATOR USAGE (groupby simulator_id)
  - SECTION 5: EXERCISE TYPE ANALYSIS (groupby exercise_type)
  - SECTION 6: JSON EXPORT (output/analysis_results.json)

Author: HuyVu
Date: September 23, 2026
"""

import pandas as pd
import json
import os
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, '../data/sample_flights.csv')
output_dir = os.path.join(script_dir, '../output')
output_file = os.path.join(output_dir, 'analysis_results.json')

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# ============================================================================
# READ CSV DATA
# ============================================================================

try:
    df = pd.read_csv(csv_file)
    print(f"✅ Successfully loaded CSV file: {csv_file}\n")
except FileNotFoundError:
    print(f"❌ Error: CSV file not found at {csv_file}")
    exit(1)

# ============================================================================
# DISPLAY ANALYSIS HEADER
# ============================================================================

print("=" * 80)
print("FLIGHT SIMULATOR TRAINING DATA - COMPREHENSIVE ANALYSIS")
print("=" * 80)
print(f"\nAnalysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Total Records: {len(df)}")
print(f"Date Range: {df['date'].min()} to {df['date'].max()}")

# ============================================================================
# SECTION 1: STUDENT PERFORMANCE ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 1: STUDENTS SUMMARY - GROUPBY student_id")
print("=" * 80)

# Group by student and calculate statistics
student_analysis = df.groupby('student_id', as_index=False).agg({
    'student_name': 'first',
    'session_id': 'count',  # Number of sessions
    'overall_score': ['mean', 'min', 'max', 'std'],
    'score_control': 'mean',
    'score_navigation': 'mean',
    'score_safety': 'mean',
    'score_communication': 'mean',
    'status': lambda x: (x == 'Pass').sum()  # Count passes
}).round(2)

# Flatten column names
student_analysis.columns = ['student_id', 'student_name', 'total_sessions', 
                           'avg_score', 'min_score', 'max_score', 'score_std',
                           'avg_control', 'avg_navigation', 'avg_safety', 'avg_communication',
                           'pass_count']

# Calculate pass rate
student_analysis['pass_rate_percent'] = (
    (student_analysis['pass_count'] / student_analysis['total_sessions'] * 100)
).round(1)

print(f"\nTotal Unique Students: {len(student_analysis)}")
print("\n" + "-" * 80)
print("STUDENT PERFORMANCE TABLE")
print("-" * 80)

# Display in readable format
for idx, row in student_analysis.iterrows():
    print(f"\n{idx+1}. {row['student_name']} ({row['student_id']})")
    print(f"   Sessions Attended:     {int(row['total_sessions'])}")
    print(f"   Overall Score (avg):   {row['avg_score']:.1f}/100")
    print(f"   Score Range:           {row['min_score']:.1f} - {row['max_score']:.1f}")
    print(f"   Score Std Dev:         {row['score_std']:.2f}")
    print(f"   Pass Count:            {int(row['pass_count'])} passes")
    print(f"   Pass Rate:             {row['pass_rate_percent']:.1f}%")
    print(f"   Skill Breakdown:")
    print(f"      - Control:         {row['avg_control']:.1f}/100")
    print(f"      - Navigation:      {row['avg_navigation']:.1f}/100")
    print(f"      - Safety:          {row['avg_safety']:.1f}/100")
    print(f"      - Communication:   {row['avg_communication']:.1f}/100")

# ============================================================================
# SECTION 2: SESSION ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 2: FLIGHT SESSIONS SUMMARY")
print("=" * 80)

print(f"\nTotal Flight Sessions: {len(df)}")

# Sessions by date
print(f"\n{'-' * 80}")
print("SESSIONS BY DATE")
print("-" * 80)
sessions_by_date = df.groupby('date').size().sort_index()
for date, count in sessions_by_date.items():
    print(f"   {date}: {count} sessions")

# Sessions by exercise type
print(f"\n{'-' * 80}")
print("SESSIONS BY EXERCISE TYPE")
print("-" * 80)
sessions_by_type = df.groupby('exercise_type').agg({
    'session_id': 'count',
    'overall_score': 'mean',
    'status': lambda x: f"{(x == 'Pass').sum()}/{len(x)}"
}).round(1)
sessions_by_type.columns = ['count', 'avg_score', 'pass_count']

for exercise_type, row in sessions_by_type.iterrows():
    print(f"   {exercise_type:20s}: {int(row['count']):2d} sessions | "
          f"Avg Score: {row['avg_score']:.1f} | Pass Rate: {row['pass_count']}")

# Sessions by difficulty level
print(f"\n{'-' * 80}")
print("SESSIONS BY DIFFICULTY LEVEL")
print("-" * 80)
sessions_by_difficulty = df.groupby('difficulty').agg({
    'session_id': 'count',
    'overall_score': 'mean',
    'status': lambda x: f"{(x == 'Pass').sum()}/{len(x)}"
}).round(1)
sessions_by_difficulty.columns = ['count', 'avg_score', 'pass_count']

for difficulty, row in sessions_by_difficulty.iterrows():
    print(f"   {difficulty:15s}: {int(row['count']):2d} sessions | "
          f"Avg Score: {row['avg_score']:.1f} | Pass Rate: {row['pass_count']}")

# ============================================================================
# SECTION 3: INSTRUCTOR WORKLOAD ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 3: INSTRUCTOR WORKLOAD - GROUPBY instructor_id")
print("=" * 80)

instructor_analysis = df.groupby('instructor_id', as_index=False).agg({
    'instructor_name': 'first',
    'session_id': 'count',
    'overall_score': 'mean',
    'status': lambda x: (x == 'Pass').sum()
}).round(1)

instructor_analysis.columns = ['instructor_id', 'instructor_name', 'total_sessions', 
                              'avg_student_score', 'student_passes']
instructor_analysis['pass_rate'] = (
    (instructor_analysis['student_passes'] / instructor_analysis['total_sessions'] * 100)
).round(1)

print(f"\nTotal Instructors: {len(instructor_analysis)}")
print("\n" + "-" * 80)

for idx, row in instructor_analysis.iterrows():
    print(f"\n{idx+1}. {row['instructor_name']} ({row['instructor_id']})")
    print(f"   Total Sessions Taught:    {int(row['total_sessions'])}")
    print(f"   Avg Student Score:        {row['avg_student_score']:.1f}/100")
    print(f"   Student Pass Rate:        {row['pass_rate']:.1f}%")
    print(f"   Students Passed:          {int(row['student_passes'])} out of {int(row['total_sessions'])}")

# ============================================================================
# SECTION 4: SIMULATOR USAGE ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 4: SIMULATOR USAGE - GROUPBY simulator_id")
print("=" * 80)

simulator_analysis = df.groupby('simulator_id', as_index=False).agg({
    'session_id': 'count',
    'duration_minutes': 'sum',
    'overall_score': 'mean',
    'status': lambda x: (x == 'Pass').sum()
}).round(1)

simulator_analysis.columns = ['simulator_id', 'total_sessions', 'total_hours', 
                             'avg_score', 'student_passes']
simulator_analysis['total_hours'] = (simulator_analysis['total_hours'] / 60).round(1)
simulator_analysis['pass_rate'] = (
    (simulator_analysis['student_passes'] / simulator_analysis['total_sessions'] * 100)
).round(1)

print(f"\nTotal Simulators: {len(simulator_analysis)}")
print("\n" + "-" * 80)

for idx, row in simulator_analysis.iterrows():
    print(f"\n{idx+1}. Simulator {row['simulator_id']}")
    print(f"   Total Sessions:    {int(row['total_sessions'])}")
    print(f"   Total Hours Used:  {row['total_hours']:.1f} hours")
    print(f"   Avg Score:         {row['avg_score']:.1f}/100")
    print(f"   Pass Rate:         {row['pass_rate']:.1f}%")

# ============================================================================
# SECTION 5: EXERCISE TYPE ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 5: EXERCISE TYPE PERFORMANCE ANALYSIS")
print("=" * 80)

exercise_analysis = df.groupby('exercise_type', as_index=False).agg({
    'session_id': 'count',
    'overall_score': 'mean',
    'score_control': 'mean',
    'score_navigation': 'mean',
    'score_safety': 'mean',
    'score_communication': 'mean',
    'status': lambda x: (x == 'Pass').sum()
}).round(2)

exercise_analysis.columns = ['exercise_type', 'total_sessions', 'avg_overall',
                            'avg_control', 'avg_navigation', 'avg_safety',
                            'avg_communication', 'pass_count']
exercise_analysis['pass_rate'] = (
    (exercise_analysis['pass_count'] / exercise_analysis['total_sessions'] * 100)
).round(1)

print(f"\nTotal Exercise Types: {len(exercise_analysis)}")
print("\n" + "-" * 80)

for idx, row in exercise_analysis.iterrows():
    print(f"\n{idx+1}. {row['exercise_type']}")
    print(f"   Sessions:          {int(row['total_sessions'])}")
    print(f"   Pass Rate:         {row['pass_rate']:.1f}%")
    print(f"   Scores:")
    print(f"      - Overall:     {row['avg_overall']:.1f}/100")
    print(f"      - Control:     {row['avg_control']:.1f}/100")
    print(f"      - Navigation:  {row['avg_navigation']:.1f}/100")
    print(f"      - Safety:      {row['avg_safety']:.1f}/100")
    print(f"      - Communication: {row['avg_communication']:.1f}/100")

# ============================================================================
# SECTION 6: EXPORT TO JSON
# ============================================================================

print("\n" + "=" * 80)
print("SECTION 6: EXPORTING ANALYSIS RESULTS TO JSON")
print("=" * 80)

# Prepare comprehensive analysis results
analysis_results = {
    "metadata": {
        "analysis_date": datetime.now().isoformat(),
        "data_source": "sample_flights.csv",
        "total_records": len(df),
        "analysis_period": {
            "start_date": str(df['date'].min()),
            "end_date": str(df['date'].max())
        }
    },
    "students": {
        "total_count": len(student_analysis),
        "data": student_analysis.to_dict('records')
    },
    "instructors": {
        "total_count": len(instructor_analysis),
        "data": instructor_analysis.to_dict('records')
    },
    "simulators": {
        "total_count": len(simulator_analysis),
        "data": simulator_analysis.to_dict('records')
    },
    "exercise_types": {
        "total_count": len(exercise_analysis),
        "data": exercise_analysis.to_dict('records')
    },
    "sessions": {
        "total_count": len(df),
        "by_date": sessions_by_date.to_dict(),
        "by_difficulty": sessions_by_difficulty.to_dict('records'),
        "by_exercise_type": sessions_by_type.to_dict('records')
    },
    "statistics": {
        "overall_pass_rate": round((df['status'] == 'Pass').sum() / len(df) * 100, 1),
        "average_score": round(df['overall_score'].mean(), 2),
        "score_range": {
            "min": float(df['overall_score'].min()),
            "max": float(df['overall_score'].max()),
            "std": round(df['overall_score'].std(), 2)
        }
    }
}

# Save to JSON file
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(analysis_results, f, indent=2, ensure_ascii=False)

print(f"\n✅ Analysis results exported to: {output_file}")
print(f"   File size: {os.path.getsize(output_file)} bytes")

# ============================================================================
# COMPLETION SUMMARY
# ============================================================================

print("\n" + "=" * 80)
print("✅ ANALYSIS COMPLETE")
print("=" * 80)

print(f"\n📊 KEY FINDINGS:")
print(f"   - Analyzed {len(df)} flight training sessions")
print(f"   - {len(student_analysis)} unique students")
print(f"   - {len(instructor_analysis)} instructors")
print(f"   - {len(simulator_analysis)} simulators")
print(f"   - {len(exercise_analysis)} exercise types")
print(f"   - Overall pass rate: {round((df['status'] == 'Pass').sum() / len(df) * 100, 1)}%")
print(f"   - Average score: {round(df['overall_score'].mean(), 1)}/100")

print(f"\n📁 OUTPUT FILES:")
print(f"   - JSON Results: {output_file}")

print(f"\n📋 NEXT STEPS:")
print(f"   1. Review the analysis results above")
print(f"   2. Check output/analysis_results.json for detailed data")
print(f"   3. Commit all files to Git")
print(f"   4. Create README.md documentation")

print("\n" + "=" * 80 + "\n")

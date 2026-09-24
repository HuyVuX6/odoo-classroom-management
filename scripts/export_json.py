"""
export_json.py - CSV to JSON Export Script
============================================

Purpose:
  Convert flight simulator training data from CSV format to JSON format.
  Creates both compact and pretty-printed JSON files for easy review.

Usage:
  python scripts/export_json.py

Expected Output:
  - data/sample_flights.json (compact format)
  - data/sample_flights_pretty.json (pretty-printed format)

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
output_dir = os.path.join(script_dir, '../data')
json_file = os.path.join(output_dir, 'sample_flights.json')
pretty_json_file = os.path.join(output_dir, 'sample_flights_pretty.json')

# ============================================================================
# READ CSV FILE
# ============================================================================

try:
    df = pd.read_csv(csv_file)
    print(f"✅ Successfully loaded CSV file: {csv_file}\n")
except FileNotFoundError:
    print(f"❌ Error: CSV file not found at {csv_file}")
    exit(1)

# ============================================================================
# CONVERT TO JSON
# ============================================================================

# Convert DataFrame to list of dictionaries (one per row)
json_data = df.to_dict(orient='records')

# Create comprehensive JSON output with metadata
output = {
    "metadata": {
        "export_date": datetime.now().isoformat(),
        "total_records": len(df),
        "data_source": "sample_flights.csv",
        "description": "Flight simulator training session data",
        "columns": list(df.columns),
        "statistics": {
            "total_students": int(df['student_id'].nunique()),
            "total_instructors": int(df['instructor_id'].nunique()),
            "total_simulators": int(df['simulator_id'].nunique()),
            "date_range": {
                "start": str(df['date'].min()),
                "end": str(df['date'].max())
            },
            "pass_count": int((df['status'] == 'Pass').sum()),
            "fail_count": int((df['status'] == 'Fail').sum())
        }
    },
    "data": json_data
}

# ============================================================================
# SAVE JSON FILES
# ============================================================================

# Save compact JSON
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False)

# Save pretty-printed JSON for easy viewing
with open(pretty_json_file, 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

# ============================================================================
# DISPLAY SUMMARY
# ============================================================================

print("=" * 80)
print("CSV TO JSON EXPORT SUMMARY")
print("=" * 80)

print(f"\n✅ EXPORT SUCCESSFUL")
print(f"   Records exported: {len(df)}")
print(f"   Compact JSON:     {os.path.getsize(json_file)} bytes")
print(f"   Pretty JSON:      {os.path.getsize(pretty_json_file)} bytes")

print(f"\n📄 OUTPUT FILES CREATED")
print(f"   1. {json_file}")
print(f"   2. {pretty_json_file}")

print(f"\n📊 DATA STATISTICS")
print(f"   Total Students:    {output['metadata']['statistics']['total_students']}")
print(f"   Total Instructors: {output['metadata']['statistics']['total_instructors']}")
print(f"   Total Simulators:  {output['metadata']['statistics']['total_simulators']}")
print(f"   Pass Records:      {output['metadata']['statistics']['pass_count']}")
print(f"   Fail Records:      {output['metadata']['statistics']['fail_count']}")
print(f"   Date Range:        {output['metadata']['statistics']['date_range']['start']} to {output['metadata']['statistics']['date_range']['end']}")

print(f"\n📋 JSON STRUCTURE")
print(f"   - metadata: Export information and statistics")
print(f"   - data: Array of {len(json_data)} flight session records")

# Display first record as example
print(f"\n📝 SAMPLE RECORD (First Session)")
print(f"   Session ID: {json_data[0]['session_id']}")
print(f"   Student: {json_data[0]['student_name']} ({json_data[0]['student_id']})")
print(f"   Instructor: {json_data[0]['instructor_name']} ({json_data[0]['instructor_id']})")
print(f"   Date: {json_data[0]['date']}")
print(f"   Exercise: {json_data[0]['exercise_type']} ({json_data[0]['difficulty']})")
print(f"   Score: {json_data[0]['overall_score']}")
print(f"   Status: {json_data[0]['status']}")

# ============================================================================
# VALIDATE JSON
# ============================================================================

print(f"\n" + "=" * 80)
print("JSON VALIDATION")
print("=" * 80)

# Try to load and re-parse the JSON to ensure it's valid
try:
    with open(json_file, 'r', encoding='utf-8') as f:
        test_load = json.load(f)
    print(f"   ✅ Compact JSON is valid and parseable")
except json.JSONDecodeError as e:
    print(f"   ❌ JSON validation failed: {e}")

try:
    with open(pretty_json_file, 'r', encoding='utf-8') as f:
        test_load = json.load(f)
    print(f"   ✅ Pretty JSON is valid and parseable")
except json.JSONDecodeError as e:
    print(f"   ❌ JSON validation failed: {e}")

# ============================================================================
# COMPLETION
# ============================================================================

print(f"\n" + "=" * 80)
print("✅ EXPORT COMPLETE")
print("=" * 80)
print(f"\nNext step: Run 'python scripts/analyze_data.py' to analyze the data")
print("=" * 80 + "\n")

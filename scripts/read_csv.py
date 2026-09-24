"""
read_csv.py - Flight Simulator Training Data CSV Reader
========================================================

Purpose:
  Read flight simulator training data from CSV file and display
  summary statistics and data analysis.

Usage:
  python scripts/read_csv.py

Expected Output:
  - Total records and columns
  - Column names and data types
  - First 5 records
  - Summary statistics
  - Unique values in key columns

Author: HuyVu
Date: September 23, 2026
"""

import pandas as pd
import os

# ============================================================================
# CONFIGURATION
# ============================================================================

# Construct path to CSV file (works from any directory)
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_dir, '../data/sample_flights.csv')

# ============================================================================
# READ CSV DATA
# ============================================================================

try:
    df = pd.read_csv(csv_file)
    print(f"✅ Successfully loaded CSV file: {csv_file}\n")
except FileNotFoundError:
    print(f"❌ Error: CSV file not found at {csv_file}")
    print("   Make sure you're running from the project root directory:")
    print("   cd odoo-classroom-management")
    print("   python scripts/read_csv.py")
    exit(1)

# ============================================================================
# DISPLAY BASIC INFORMATION
# ============================================================================

print("=" * 80)
print("FLIGHT SIMULATOR TRAINING DATA - CSV ANALYSIS")
print("=" * 80)

print(f"\n📊 DATA SUMMARY")
print(f"   Total Records: {len(df)}")
print(f"   Total Columns: {len(df.columns)}")
print(f"   File Size: {os.path.getsize(csv_file)} bytes")

print(f"\n📋 COLUMN NAMES ({len(df.columns)} columns):")
for i, col in enumerate(df.columns, 1):
    print(f"   {i:2d}. {col:30s} ({df[col].dtype})")

# ============================================================================
# DISPLAY FIRST RECORDS
# ============================================================================

print("\n" + "=" * 80)
print("FIRST 5 RECORDS")
print("=" * 80)
print(df.head().to_string())

print("\n" + "=" * 80)
print("LAST 5 RECORDS")
print("=" * 80)
print(df.tail().to_string())

# ============================================================================
# DATA TYPES
# ============================================================================

print("\n" + "=" * 80)
print("DATA TYPES")
print("=" * 80)
print(df.dtypes)

# ============================================================================
# SUMMARY STATISTICS
# ============================================================================

print("\n" + "=" * 80)
print("SUMMARY STATISTICS (Numeric Columns)")
print("=" * 80)
print(df.describe().to_string())

# ============================================================================
# UNIQUE VALUES IN KEY COLUMNS
# ============================================================================

print("\n" + "=" * 80)
print("UNIQUE VALUES IN KEY COLUMNS")
print("=" * 80)

unique_cols = {
    'Students': 'student_id',
    'Student Names': 'student_name',
    'Instructors': 'instructor_id',
    'Instructor Names': 'instructor_name',
    'Simulators': 'simulator_id',
    'Exercise Types': 'exercise_type',
    'Difficulty Levels': 'difficulty',
    'Status Values': 'status'
}

for label, col in unique_cols.items():
    unique_vals = df[col].unique()
    print(f"\n{label} ({len(unique_vals)}):")
    for val in unique_vals:
        count = (df[col] == val).sum()
        print(f"   - {val:20s} (appears {count} times)")

# ============================================================================
# DATE RANGE
# ============================================================================

print("\n" + "=" * 80)
print("DATE RANGE")
print("=" * 80)
dates = pd.to_datetime(df['date'])
print(f"   Earliest date: {dates.min()}")
print(f"   Latest date:   {dates.max()}")
print(f"   Date range:    {(dates.max() - dates.min()).days} days")

# ============================================================================
# MISSING VALUES
# ============================================================================

print("\n" + "=" * 80)
print("MISSING VALUES CHECK")
print("=" * 80)
missing = df.isnull().sum()
if missing.sum() == 0:
    print("   ✅ No missing values found in the dataset")
else:
    print("   Missing values by column:")
    for col, count in missing[missing > 0].items():
        print(f"   - {col}: {count} missing values")

# ============================================================================
# COMPLETION
# ============================================================================

print("\n" + "=" * 80)
print("✅ CSV ANALYSIS COMPLETE")
print("=" * 80)
print(f"\nDataFrame shape: {df.shape[0]} rows × {df.shape[1]} columns")
print("\nNext step: Run 'python scripts/export_json.py' to export to JSON")
print("=" * 80 + "\n")

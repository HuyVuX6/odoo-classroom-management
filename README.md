# Odoo Classroom Management System
## Flight Simulator Training with AI-Driven Analysis

**Status:** Week 1 - Foundation (In Progress)  
**Deadline:** September 27, 2026  
**Project Lead:** HuyVu  
**Goal:** Business Analyst Position at Google

---

## 🎯 Project Overview

This project implements a comprehensive Odoo-based classroom management system for flight simulator training programs. It combines enterprise resource planning (ERP) capabilities with AI-driven data analysis to optimize student learning outcomes and instructor efficiency.

### Key Objectives
- ✅ **Week 1:** Build data pipeline (CSV → JSON → Analysis)
- 🔄 **Week 2:** Implement data import validation and duplicate detection
- 📅 **Weeks 3-8:** Develop Odoo models, AI analysis, and reporting dashboards

---

## 📊 Current Status: Week 1

### Week 1 Deliverables
- ✅ Git repository created (public for portfolio)
- ✅ Python scripts for data processing
- ✅ Sample flight training data (10 sessions, 5 students)
- ✅ CSV-to-JSON conversion pipeline
- ✅ Comprehensive data analysis with groupby operations
- ✅ Documentation and requirements file

### Week 1 Completion: [0%]
- [ ] Scripts created and tested
- [ ] Sample data validated
- [ ] Git commits completed
- [ ] README documentation finished
- [ ] Ready for Week 2

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (version control)
- ~30 MB disk space for project files

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/odoo-classroom-management.git
cd odoo-classroom-management
```

#### 2. Create Project Structure
```bash
# The folders should already exist after cloning
# If not, create them:
mkdir -p data scripts output
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- `pandas` - Data manipulation and analysis
- `openpyxl` - Excel file support (for future use)

#### 4. Verify Installation
```bash
python scripts/read_csv.py
```

You should see output showing 10 flight records and 5 students.

---

## 📁 Project Structure

```
odoo-classroom-management/
│
├── README.md                        # This file - project documentation
├── .gitignore                       # Git ignore patterns
├── requirements.txt                 # Python dependencies
│
├── data/
│   ├── sample_flights.csv          # Sample training data (10 sessions)
│   ├── sample_flights.json         # Exported JSON format
│   └── sample_flights_pretty.json  # Pretty-printed JSON for review
│
├── scripts/
│   ├── read_csv.py                 # Task 2: Read and analyze CSV
│   ├── export_json.py              # Task 3: Convert CSV to JSON
│   └── analyze_data.py             # Task 4: Comprehensive data analysis
│
└── output/
    └── analysis_results.json       # Task 4: Analysis results export
```

---

## 🐍 Python Scripts

### 1. read_csv.py - Read Flight Data
**Purpose:** Load and analyze CSV data  
**Time to run:** ~1 second  
**Dependencies:** pandas

```bash
python scripts/read_csv.py
```

**Output includes:**
- Total records and columns
- All column names with data types
- First and last 5 records
- Summary statistics for numeric columns
- Unique values in key columns (students, instructors, simulators)
- Date range

**Example output:**
```
Total Records: 10
Total Columns: 18

Unique Students: 5
Unique Instructors: 2
Unique Simulators: 3
Date Range: 2026-09-15 to 2026-09-19
```

---

### 2. export_json.py - Export to JSON
**Purpose:** Convert CSV data to JSON format with metadata  
**Time to run:** ~1 second  
**Dependencies:** pandas, json  

```bash
python scripts/export_json.py
```

**Creates:**
- `data/sample_flights.json` - Compact JSON
- `data/sample_flights_pretty.json` - Pretty-printed JSON

**Output includes:**
- Metadata (export date, total records, statistics)
- Complete flight session records
- Summary statistics (pass count, date range, etc.)

**JSON Structure:**
```json
{
  "metadata": {
    "export_date": "2026-09-23T10:45:30",
    "total_records": 10,
    "data_source": "sample_flights.csv",
    "statistics": {
      "total_students": 5,
      "total_instructors": 2,
      "pass_count": 9,
      "fail_count": 1
    }
  },
  "data": [
    {
      "session_id": "S001",
      "student_name": "Nguyen Van A",
      "overall_score": 79,
      "status": "Pass",
      ...
    }
  ]
}
```

---

### 3. analyze_data.py - Comprehensive Analysis
**Purpose:** Analyze data using groupby operations to distinguish students from sessions  
**Time to run:** ~2 seconds  
**Dependencies:** pandas, json  

```bash
python scripts/analyze_data.py
```

**Creates:** `output/analysis_results.json` with comprehensive analysis

**Analysis Sections:**

#### Section 1: Student Performance (groupby student_id)
- Total sessions per student
- Average/min/max scores
- Pass rates
- Skill breakdown (control, navigation, safety, communication)

Example:
```
1. Nguyen Van A (ST001)
   Sessions Attended:     2
   Overall Score (avg):   81.0/100
   Pass Rate:             100.0%
   Skills: Control 81.0 | Navigation 78.0 | Safety 84.0 | Communication 81.0
```

#### Section 2: Session Analysis
- Total flights by date
- Sessions by exercise type (Takeoff, Landing, Navigation, Emergency)
- Sessions by difficulty (Beginner, Intermediate, Advanced)
- Performance breakdown by category

#### Section 3: Instructor Workload (groupby instructor_id)
- Total sessions taught
- Average student scores
- Student pass rates per instructor
- Instructor effectiveness metrics

#### Section 4: Simulator Usage (groupby simulator_id)
- Total sessions per simulator
- Hours of utilization
- Performance on each simulator
- Simulator efficiency metrics

#### Section 5: Exercise Type Performance
- Performance by exercise type
- Pass rates for each exercise
- Difficulty level comparison

#### Section 6: JSON Export
- All analysis results saved to `output/analysis_results.json`
- Structured for further analysis or dashboard integration

---

## 📊 Sample Data

### Overview
The project includes realistic flight simulator training data:

| Metric | Value |
|--------|-------|
| Flight Sessions | 10 (S001-S010) |
| Students | 5 (ST001-ST005) |
| Instructors | 2 (IN001, IN002) |
| Simulators | 3 (SIM001-SIM003) |
| Date Range | Sept 15-19, 2026 |
| Exercise Types | Takeoff, Landing, Navigation, Emergency |
| Difficulty Levels | Beginner, Intermediate, Advanced |

### Data Fields

Each flight session record includes:

**Session Information**
- `session_id` - Unique session identifier (S001-S010)
- `date` - Training date (YYYY-MM-DD)
- `start_time` - Session start time (HH:MM)
- `end_time` - Session end time (HH:MM)
- `duration_minutes` - Session duration in minutes

**People Information**
- `student_id` - Unique student identifier
- `student_name` - Student name (Vietnamese)
- `instructor_id` - Unique instructor identifier
- `instructor_name` - Instructor name

**Equipment Information**
- `simulator_id` - Flight simulator identifier
- `exercise_type` - Type of exercise (Takeoff, Landing, etc.)
- `difficulty` - Exercise difficulty level

**Performance Scores (0-100 scale)**
- `score_control` - Aircraft control proficiency
- `score_navigation` - Navigation and route planning
- `score_safety` - Safety procedure adherence
- `score_communication` - Radio communication clarity
- `overall_score` - Aggregate performance score
- `status` - Pass/Fail result

### Sample Records

| Session | Student | Instructor | Exercise | Score | Status |
|---------|---------|-----------|----------|-------|--------|
| S001 | Nguyen Van A | Tran Thi B | Takeoff | 79 | Pass |
| S002 | Pham Thi C | Tran Thi B | Landing | 82 | Pass |
| S003 | Hoang Van D | Le Minh E | Navigation | 71 | Fail |
| S004 | Vu Thi F | Le Minh E | Emergency | 87 | Pass |
| S005 | Nguyen Van A | Tran Thi B | Navigation | 83 | Pass |

---

## 🎓 Data Model Overview

This project is based on a comprehensive 12-entity data model with 115 optimized fields:

### Core Entities
1. **Students** - Trainee information and progress
2. **Flight Sessions** - Individual training events
3. **Instructors** - Training personnel
4. **Simulators** - Flight training equipment
5. **Exercise Types** - Training exercise definitions
6. **Performance Scores** - Individual skill assessments
7. **AI Analysis Results** - Automated performance analysis
8. **Certifications** - Student qualifications
9. **Classes** - Training groups
10. **Schedules** - Training timetables
11. **Equipment Maintenance** - Simulator upkeep logs
12. **Reports** - Training analytics

**Data Optimization:** 41% reduction in fields (195 → 115) through intelligent consolidation

For detailed model information, see: `Final_Data_Model_Review.md`

---

## 🔄 Data Processing Pipeline

### Week 1 Pipeline (This Week)
```
CSV File
  ↓ (read_csv.py)
Pandas DataFrame
  ↓ (export_json.py)
JSON File
  ↓ (analyze_data.py)
Analysis Results
```

### Week 2 Pipeline (Next Week)
```
Import Validation
  ↓
External_Session_ID Check (Proposal 1)
  ↓
File_Hash Verification (Proposal 2)
  ↓
Database Insertion
```

### Weeks 3-8 Pipeline
```
Odoo Models
  ↓
AI Analysis Module
  ↓
Dashboard & Reports
  ↓
Student Certifications
```

---

## 💡 Key Features & Proposals

### Proposal 1: External_Session_ID
**Purpose:** Prevent duplicate session imports  
**Implementation:** Unique identifier from external flight system  
**Benefit:** Ensures data consistency across systems

### Proposal 2: File_Hash
**Purpose:** Prevent re-import of identical files  
**Implementation:** MD5/SHA256 hash of imported data  
**Benefit:** Tracks data import history and prevents duplicates

### Proposal 3: Separate AI Score Columns
**Purpose:** Enable fast analytics without JSON parsing  
**Implementation:** Individual Float columns for each skill area  
**Benefit:** Real-time dashboard updates and indexed queries

---

## 🧪 Testing Your Setup

### Quick Test (1 minute)
```bash
# All three scripts should run without errors
python scripts/read_csv.py
python scripts/export_json.py
python scripts/analyze_data.py
```

### Verify Output Files (2 minutes)
```bash
# Check that files were created
ls -lh data/sample_flights.json
ls -lh output/analysis_results.json

# Verify JSON is valid
python -m json.tool data/sample_flights.json > /dev/null && echo "✅ JSON is valid"
```

### View Results
```bash
# Pretty-print JSON to console
cat data/sample_flights_pretty.json | head -50

# Count records in JSON
python -c "import json; f=json.load(open('data/sample_flights.json')); print(f'Records: {len(f[\"data\"])}')"
```

---

## 📚 Development Timeline

### ✅ Week 1: Python & Data Design (Sept 23-27)
- Create Git repository
- Build data processing scripts
- Prepare sample data
- Analysis with groupby operations
- **Status:** In Progress

### 🔄 Week 2: Data Import & Duplicate Detection (Sept 30-Oct 4)
- Implement External_Session_ID validation
- Prevent duplicate session imports
- Data import validation logic

### 📅 Week 3: Odoo Models & Forms (Oct 7-11)
- Create Odoo models based on data model
- Build forms for data entry
- Configure relationships

### 📊 Week 4: AI Analysis Module (Oct 14-18)
- Implement AI analysis logic
- Performance prediction algorithms

### 📈 Week 5: Dashboards & Reporting (Oct 21-25)
- Build student performance dashboards
- Instructor effectiveness reports

### 🏆 Week 6: Certification System (Oct 28-Nov 1)
- Implement certification logic
- Grade tracking system

### 🔗 Week 7: Advanced Features (Nov 4-8)
- System integration and optimization

### 🚀 Week 8: Final Testing & Deployment (Nov 11-15)
- Quality assurance
- Deployment preparation

---

## 💻 Technology Stack

### Data Processing
- **Python 3.8+** - Core programming language
- **Pandas** - Data manipulation and groupby operations
- **JSON** - Data serialization

### Version Control
- **Git** - Source code management
- **GitHub** - Repository hosting

### Enterprise Systems (Weeks 3-8)
- **Odoo 15+** - ERP platform
- **PostgreSQL** - Database backend
- **Python Backend** - AI analysis module

### Future Components
- **Machine Learning** - Performance prediction
- **Flask/FastAPI** - REST API
- **Vue.js/React** - Frontend dashboards
- **Docker** - Containerization

---

## 🎯 Learning Outcomes

By completing this project, you'll develop:

### Technical Skills
- ✅ Python: pandas, JSON, file I/O operations
- ✅ Data Analysis: groupby, aggregation, pivot operations
- ✅ Git/GitHub: version control and collaboration
- ✅ ERP Systems: Odoo data modeling
- ✅ Database Design: Entity relationships, optimization
- ✅ API Development: REST endpoints (Week 3+)
- ✅ Machine Learning: AI analysis module (Week 4+)

### Business Analysis Skills
- ✅ Data Modeling: 115-field optimized schema
- ✅ Requirements Analysis: Proposal evaluation
- ✅ Solution Design: Multi-tier architecture
- ✅ Performance Analysis: Student tracking and metrics
- ✅ Process Optimization: Training efficiency

### Professional Skills
- ✅ Documentation: README, comments, technical writing
- ✅ Project Management: Week-by-week breakdown
- ✅ Code Quality: PEP 8, error handling, testing
- ✅ Communication: Clear, technical explanations
- ✅ Portfolio Building: Impressive GitHub project

---

## 🚦 Quick Start Commands

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/odoo-classroom-management.git
cd odoo-classroom-management

# Install dependencies
pip install -r requirements.txt

# Run all scripts
python scripts/read_csv.py
python scripts/export_json.py
python scripts/analyze_data.py

# View results
cat output/analysis_results.json | python -m json.tool | head -50

# Git workflow
git add .
git commit -m "Week 1: Complete data pipeline"
git push origin main
```

---

## ⚠️ Troubleshooting

### Problem: "Module pandas not found"
```bash
# Solution:
pip install pandas
pip install -r requirements.txt
```

### Problem: "CSV file not found"
```bash
# Make sure you're in the project root:
cd odoo-classroom-management

# Check file exists:
ls -l data/sample_flights.csv

# Run from project root:
python scripts/read_csv.py
```

### Problem: JSON is not valid
```bash
# Verify JSON syntax:
python -m json.tool data/sample_flights.json

# If broken, re-run export:
python scripts/export_json.py
```

### Problem: Analysis script fails
```bash
# Check that output folder exists:
mkdir -p output

# Re-run analysis:
python scripts/analyze_data.py
```

### Problem: Git push fails
```bash
# Configure Git first time:
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Then try push again:
git push origin main
```

---

## 📖 Documentation Files

- **README.md** - This file (project overview and setup)
- **WEEK_1_QUICK_START.md** - 5-minute quick reference
- **WEEK_1_DETAILED_PLAN.md** - Complete implementation guide
- **Final_Data_Model_Review.md** - 12-entity data model details
- **Phân_Tích_DATA.docx** - Official data model document (Vietnamese)

---

## 🤝 Contributing

This is a portfolio project, but contributions are welcome for learning purposes:

1. **Fork** the repository
2. **Create a feature branch**: `git checkout -b feature/your-feature`
3. **Make your changes** with clear commit messages
4. **Push to GitHub**: `git push origin feature/your-feature`
5. **Create a Pull Request** with description

### Code Standards
- Follow PEP 8 Python style guide
- Add comments for complex logic
- Update documentation with changes
- Test before committing

---

## 📈 Portfolio Value

This project demonstrates to Google's Business Analyst team:

✅ **Technical Competency**
- Full-stack Python development
- Data pipeline design and implementation
- Database schema optimization (41% field reduction)
- Version control and Git workflow

✅ **Business Analysis Skills**
- Requirements analysis (Proposal evaluation)
- Data modeling and optimization
- Solution design and architecture
- Performance metrics and KPIs

✅ **Problem-Solving**
- End-to-end project design
- Scalable architecture
- Attention to data quality
- Comprehensive documentation

✅ **Professional Communication**
- Clear README and documentation
- Meaningful commit messages
- Code comments and explanations
- Project structure and organization

---

## 📞 Support & Questions

**Project Lead:** HuyVu  
**Email:** [your.email@example.com]  
**GitHub:** [@YOUR_USERNAME]

---

## 📋 License

MIT License - This project is open source and available for educational and commercial use.

See LICENSE file for details.

---

## 🙏 Acknowledgments

This project is developed as part of an 8-week intensive program focusing on:
- Enterprise Resource Planning (ERP) System Design
- Data Modeling and Optimization
- AI-Driven Business Analytics
- Flight Simulator Training Management

**Project Goal:** Demonstrate readiness for Business Analyst position at Google  
**Timeline:** September-November 2026  
**Status:** Week 1 - Foundation Phase

---

**Last Updated:** September 23, 2026  
**Project Status:** In Progress - Week 1  
**Next Milestone:** Week 1 Completion (September 27, 2026)

🚀 **Happy coding! This is your foundation for an amazing 8-week journey!** ✈️📊

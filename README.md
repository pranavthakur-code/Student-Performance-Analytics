# 📊 Student Performance Analytics System

A Python-based data analysis project that analyzes student academic performance using **Python, Pandas, and NumPy**.

The system processes student marks and attendance data to calculate total marks, average marks, grades, pass/fail status, subject-wise performance, attendance statistics, and identify top-performing students.

---

## 📌 Project Overview

The **Student Performance Analytics System** is designed to analyze student academic performance using data stored in a CSV file.

It uses Pandas to organize and analyze student records and NumPy to perform numerical and statistical calculations.

The project demonstrates how Python can be used to process real-world data and generate meaningful insights.

### What Does This Project Do?

- Calculates total marks for each student.
- Calculates average marks.
- Assigns grades based on average marks.
- Determines Pass/Fail status.
- Calculates overall class performance statistics.
- Analyzes subject-wise performance.
- Identifies the top 5 performing students.
- Analyzes student attendance.
- Identifies students with low attendance.
- Performs statistical analysis using NumPy.

---

## 🎯 Objectives

The main objectives of this project are:

- Analyze student academic performance.
- Calculate total and average marks.
- Assign grades using conditional statements.
- Identify Pass/Fail status.
- Find top-performing students.
- Perform subject-wise analysis.
- Analyze student attendance.
- Perform statistical calculations using NumPy.
- Practice Python functions and data processing.
- Understand how Pandas DataFrames are used for data analysis.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Reading, organizing, filtering, and analyzing data |
| NumPy | Numerical calculations and statistical analysis |
| CSV | Storing student records |
| GitHub | Project version control and sharing |

---

## 📦 Python Libraries

### 1. Pandas

Pandas is a Python library used to work with structured data.

In this project, Pandas is used to:

- Read student records from a CSV file.
- Create and manage a DataFrame.
- Calculate averages.
- Sort and filter student records.
- Analyze marks and attendance.

### 2. NumPy

NumPy is a Python library used for numerical calculations.

In this project, NumPy is used to:

- Calculate the mean.
- Find maximum and minimum values.
- Calculate standard deviation.
- Perform numerical operations on student performance data.

---

## 📂 Project Structure

```text
Student-Performance-Analytics/
│
├── data/
│   └── students.csv
│
├── main.py
├── functions.py
├── requirements.txt
└── README.md
```

### File Description

| File/Folder | Description |
|---|---|
| `data/students.csv` | Contains student marks and attendance records |
| `main.py` | Main file used to execute the project |
| `functions.py` | Contains reusable functions for calculations and analysis |
| `requirements.txt` | Lists the external Python libraries required by the project |
| `README.md` | Contains project documentation |

---

## 📊 Dataset Description

The project uses a CSV dataset containing student academic information.

The dataset contains **20 student records**.

### Dataset Columns

| Column | Description |
|---|---|
| `Student_ID` | Unique identification number of each student |
| `Name` | Student's name |
| `Department` | Student's department |
| `Python Marks` | Marks obtained in Python |
| `Data Structures Marks` | Marks obtained in Data Structures |
| `Java Marks` | Marks obtained in Java |
| `Attendance` | Student attendance percentage |

The dataset is stored in `data/students.csv` and loaded into a Pandas DataFrame for analysis.

---

## ⚙️ Project Features

### 1. Student Data Loading

The program loads student records from the CSV file using Pandas.

```python
df = pd.read_csv("data/students.csv")
```

### 2. Total Marks Calculation

The program calculates total marks by adding marks from all three subjects.

**Formula:**

```text
Total Marks = Python Marks + Data Structures Marks + Java Marks
```

### 3. Average Marks Calculation

The average marks are calculated by dividing total marks by the number of subjects.

**Formula:**

```text
Average Marks = Total Marks / 3
```

The average is rounded to two decimal places.

### 4. Grade Calculation

The program assigns grades according to each student's average marks.

| Average Marks | Grade |
|---|---|
| 90 or above | A+ |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| 50 to below 60 | D |
| Below 50 | F |

### 5. Pass/Fail Status

The program determines the student's status using the following rule:

- Average marks greater than or equal to 50: **Pass**
- Average marks below 50: **Fail**

*Note: This project uses average marks as its simplified pass/fail rule.*

### 6. Class Performance Statistics

The program calculates:

- Highest average marks.
- Lowest average marks.
- Overall class average.
- Number of passed students.
- Number of failed students.

### 7. Subject-wise Analysis

The program calculates average marks for:

- Python.
- Data Structures.
- Java.

This helps compare the overall performance across subjects.

### 8. Top Performing Students

The program sorts students by average marks in descending order and displays the top 5 students.

### 9. Attendance Analysis

The program calculates:

- Average attendance.
- Highest attendance.
- Lowest attendance.
- Students with attendance below 75%.

### 10. NumPy Statistical Analysis

The project uses NumPy to calculate:

- Mean of student average marks.
- Maximum average marks.
- Minimum average marks.
- Standard deviation of average marks.

These statistics help summarize student performance.

---

## 🧩 Python Concepts Used

This project demonstrates the following concepts:

| Concept | How It Is Used |
|---|---|
| Variables | Store marks, averages, and calculated results |
| Data Types | Handle numerical and text data |
| Conditional Statements | Assign grades and Pass/Fail status |
| Functions | Organize calculations into reusable blocks |
| Pandas DataFrame | Store and analyze student records |
| Data Filtering | Find students with low attendance |
| Data Sorting | Identify top-performing students |
| NumPy Arrays | Perform numerical calculations |
| Statistical Functions | Calculate mean, minimum, maximum, and standard deviation |
| Modular Programming | Separate reusable functions into `functions.py` |

---

## 📈 Sample Results

The following results are based on the current dataset.

### Class Statistics

```text
Highest Average Marks : 94.33
Lowest Average Marks  : 46.33
Class Average         : 75.15

Passed Students       : 18
Failed Students       : 2

Average Attendance    : 85.15%
```

### Subject-wise Average Marks

```text
Python          : 74.80
Data Structures : 75.20
Java            : 75.45
```

### Top 5 Students

```text
1. Isha Kapoor   - 94.33 - A+
2. Anjali Gupta  - 93.00 - A+
3. Aditya Rao    - 91.67 - A+
4. Priya Singh   - 89.67 - A
5. Sneha Jain    - 87.33 - A
```

*Note: These are sample results from the current dataset. Results may change if the dataset is modified.*

---

## 📋 Requirements

Before running the project, make sure Python is installed on your computer.

The `requirements.txt` file lists the external libraries used by the project.

Its contents are:

```text
pandas
numpy
```

### Why Is requirements.txt Used?

It helps other users identify and install the libraries needed to run the project.

Instead of installing each library separately, users can install all listed dependencies with one command.

---

## ▶️ How to Run the Project

Follow these steps to run the project on your computer.

### Step 1: Clone the Repository

Clone the GitHub repository or download the project files.

### Step 2: Open the Project Folder

Open the project folder in VS Code or another Python editor.

### Step 3: Open the Terminal

Open a terminal inside the project folder.

### Step 4: Install Required Libraries

Run the following command:

```bash
pip install -r requirements.txt
```

### Step 5: Run the Project

Execute the main Python file:

```bash
python main.py
```

The program will display student performance analysis in the terminal.

**Important:** Run the command from the project root folder so that the program can locate `data/students.csv`.

---

## 🔄 Project Workflow

The project follows this workflow:

```text
Student CSV Dataset
        |
        v
Load Data Using Pandas
        |
        v
Calculate Total Marks
        |
        v
Calculate Average Marks
        |
        v
Assign Grades and Status
        |
        v
Analyze Class Performance
        |
        v
Analyze Subject-wise Marks
        |
        v
Analyze Attendance
        |
        v
Identify Top Students
        |
        v
Calculate NumPy Statistics
        |
        v
Display Results
```

---

## 🧠 Learning Outcomes

Through this project, I practiced and learned:

- Python programming fundamentals.
- Working with variables and data types.
- Using conditional statements.
- Creating and calling functions.
- Reading CSV files using Pandas.
- Working with DataFrames.
- Filtering and sorting data.
- Performing calculations with NumPy.
- Understanding basic statistical analysis.
- Organizing code into multiple Python files.
- Managing project dependencies.
- Writing project documentation.
- Preparing a project repository for GitHub.

---

## 🚀 Future Improvements

Possible improvements for future versions include:

- Data visualization using Matplotlib.
- Department-wise performance comparison.
- Graphs showing subject-wise averages.
- Adding more subjects and student records.
- Exporting analysis reports.
- An interactive dashboard.
- Options to add or update student records.

These are possible future enhancements and are not part of the current version.

---

## 👨‍💻 Author

**Pranav Thakur**

Python with AI Internship Project

**Project:** Student Performance Analytics System

---

## 📄 Project Status

**Status:** Completed

The current version analyzes student marks and attendance using Python, Pandas, and NumPy.

---

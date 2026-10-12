import pandas as pd

from functions import (
    calculate_grade,
    calculate_status,
    calculate_total_marks,
    calculate_average,
    calculate_class_statistics,
    calculate_subject_averages,
    get_top_students,
    calculate_attendance_statistics,
    get_low_attendance_students,
    calculate_numpy_statistics
)

# LOAD DATASET
df = pd.read_csv("data/students.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

print("===== STUDENT PERFORMANCE DATA =====")
print(df)

# TOTAL AND AVERAGE MARKS

df["Total_Marks"] = calculate_total_marks(df)
df["Average_Marks"] = calculate_average(df["Total_Marks"])

print("\n===== STUDENT MARKS SUMMARY =====")

print(
    df[
        [
            "Student_ID",
            "Name",
            "Total_Marks",
            "Average_Marks"
        ]
    ]
)


# GRADE AND PASS/FAIL

df["Grade"] = df["Average_Marks"].apply(calculate_grade)
df["Status"] = df["Average_Marks"].apply(calculate_status)

print("\n===== GRADE & RESULT =====")

print(
    df[
        [
            "Student_ID",
            "Name",
            "Average_Marks",
            "Grade",
            "Status"
        ]
    ]
)


# CLASS PERFORMANCE

highest, lowest, class_average, passed, failed = (
    calculate_class_statistics(df)
)

print("\n===== CLASS PERFORMANCE ANALYSIS =====")

print("Highest Average:", highest)
print("Lowest Average:", lowest)
print("Overall Class Average:", round(class_average, 2))
print("Number of Passed Students:", passed)
print("Number of Failed Students:", failed)

# SUBJECT-WISE PERFORMANCE

subject_averages = calculate_subject_averages(df)

print("\n===== SUBJECT-WISE PERFORMANCE =====")

for subject, average in subject_averages.items():
    print(subject + " Average:", round(average, 2))

best_subject = max(
    subject_averages,
    key=subject_averages.get
)

print("Best Performing Subject:", best_subject)
print(
    "Best Subject Average:",
    round(subject_averages[best_subject], 2)
)

# TOP 5 STUDENTS

top_students = get_top_students(df)

print("\n===== TOP 5 PERFORMING STUDENTS =====")

print(
    top_students[
        [
            "Student_ID",
            "Name",
            "Average_Marks",
            "Grade",
            "Status"
        ]
    ]
)

# ATTENDANCE ANALYSIS

average_attendance, highest_attendance, lowest_attendance = (
    calculate_attendance_statistics(df)
)

print("\n===== ATTENDANCE ANALYSIS =====")

print(
    "Average Attendance:",
    round(average_attendance, 2),
    "%"
)

print(
    "Highest Attendance:",
    highest_attendance,
    "%"
)

print(
    "Lowest Attendance:",
    lowest_attendance,
    "%"
)

# LOW ATTENDANCE STUDENTS

low_attendance = get_low_attendance_students(df)

print("\n===== LOW ATTENDANCE STUDENTS =====")

print(
    low_attendance[
        [
            "Student_ID",
            "Name",
            "Attendance"
        ]
    ]
)

# NUMPY STATISTICAL ANALYSIS

numpy_mean, numpy_max, numpy_min, numpy_std = (
    calculate_numpy_statistics(df)
)

print("\n===== NUMPY STATISTICAL ANALYSIS =====")

print(
    "Mean of Average Marks:",
    round(numpy_mean, 2)
)

print(
    "Maximum Average Marks:",
    round(numpy_max, 2)
)

print(
    "Minimum Average Marks:",
    round(numpy_min, 2)
)

print(
    "Standard Deviation:",
    round(numpy_std, 2)
)
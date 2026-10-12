import numpy as np


# Function to calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Function to calculate pass/fail status
def calculate_status(average):
    if average >= 50:
        return "Pass"
    else:
        return "Fail"


# Function to calculate total marks
def calculate_total_marks(dataframe):
    return (
        dataframe["Python Marks"]
        + dataframe["Data Structures Marks"]
        + dataframe["Java Marks"]
    )


# Function to calculate average marks
def calculate_average(total_marks):
    return (total_marks / 3).round(2)


# Function to find class statistics
def calculate_class_statistics(dataframe):
    highest = dataframe["Average_Marks"].max()
    lowest = dataframe["Average_Marks"].min()
    average = dataframe["Average_Marks"].mean()

    passed = (dataframe["Status"] == "Pass").sum()
    failed = (dataframe["Status"] == "Fail").sum()

    return highest, lowest, average, passed, failed


# Function to calculate subject averages
def calculate_subject_averages(dataframe):
    return {
        "Python": dataframe["Python Marks"].mean(),
        "Data Structures": dataframe["Data Structures Marks"].mean(),
        "Java": dataframe["Java Marks"].mean()
    }


# Function to get top students
def get_top_students(dataframe, number=5):
    return dataframe.sort_values(
        by="Average_Marks",
        ascending=False
    ).head(number)


# Function to calculate attendance statistics
def calculate_attendance_statistics(dataframe):
    average = dataframe["Attendance"].mean()
    highest = dataframe["Attendance"].max()
    lowest = dataframe["Attendance"].min()

    return average, highest, lowest


# Function to get low attendance students
def get_low_attendance_students(dataframe, limit=75):
    return dataframe[dataframe["Attendance"] < limit]


# Function for NumPy statistical analysis
def calculate_numpy_statistics(dataframe):

    marks_array = dataframe["Average_Marks"].to_numpy()

    mean = np.mean(marks_array)
    maximum = np.max(marks_array)
    minimum = np.min(marks_array)
    standard_deviation = np.std(marks_array)

    return mean, maximum, minimum, standard_deviation
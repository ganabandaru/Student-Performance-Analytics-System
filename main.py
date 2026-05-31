import pandas as pd
df = pd.read_csv("student_data.csv")

while True:

    print("\n===== STUDENT PERFORMANCE ANALYTICS SYSTEM =====")
    print("1. Print Topper Students")
    print("2. Print Average Marks")
    print("3. Failed Students")
    print("4. Show Students With Zero Failures")
    print("5. Show Students With High Absences")
    print("6. Gender-wise Average Marks")
    print("7. Search Student By Age")
    print("8. Exit")

    choice = input("Enter your choice: ")


    if choice == "1":

        topper = df[df["G3"] == df["G3"].max()]

        print("\n===== TOPPER STUDENT =====")
        print(topper[["sex", "age", "G3"]])


    elif choice == "2":

        average = df["G3"].mean()

        print("\nAverage G3 Marks:", average)


    elif choice == "3":

        failed = df[df["G3"] < 10]

        print("\n===== FAILED STUDENTS =====")
        print(failed[["sex", "age", "G3"]])


    elif choice == "4":

        zero_fail = df[df["failures"] == 0]

        print("\n===== STUDENTS WITH ZERO FAILURES =====")
        print(zero_fail[["sex", "age", "failures", "G3"]])


    elif choice == "5":

        high_absence = df[df["absences"] > 10]

        print("\n===== STUDENTS WITH HIGH ABSENCES =====")
        print(high_absence[["sex", "age", "absences", "G3"]])


    elif choice == "6":

        average_marks = df.groupby("sex")["G3"].mean()

        print("\n===== GENDER-WISE AVERAGE MARKS =====")
        print(average_marks)


    elif choice == "7":

        age = int(input("Enter Age: "))

        student_age = df[df["age"] == age]

        print("\n===== STUDENTS FOUND =====")
        print(student_age[["sex", "age", "G3"]])


    elif choice == "8":

        print("\nProgram Exited Successfully")
        break


    else:

        print("\nPlease Enter a Valid Choice")

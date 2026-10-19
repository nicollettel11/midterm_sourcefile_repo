def classify_grade(grade):
    if grade >= 90:
        classification = "Excellent"
        status = "Passed"
    elif grade >= 85:
        classification = "Very Good"
        status = "Passed"
    elif grade >= 80:
        classification = "Good"
        status = "Passed"
    elif grade >= 75:
        classification = "Satisfactory"
        status = "Passed"
    else:
        classification = "Needs Improvement"
        status = "Failed"

    return classification, status


def load_students(filename):
    students = []

    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                if line.startswith("#"):
                    continue

                fields = line.split(",")

                if len(fields) != 3:
                    continue

                student_id, name, grade_text = fields
                student_id = student_id.strip()
                name = name.strip()
                grade_text = grade_text.strip()

                try:
                    grade = float(grade_text)
                except ValueError:
                    continue

                if grade < 0 or grade > 100:
                    continue

                students.append({
                    "student_id": student_id,
                    "name": name,
                    "grade": grade
                })

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except OSError as error:
        print(f"Error: Could not read the file '{filename}'. ({error})")

    return students


def calculate_statistics(students):
    if not students:
        return None

    total_grade = 0
    passed_count = 0
    failed_count = 0
    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        grade = student["grade"]
        total_grade += grade

        _, status = classify_grade(grade)
        if status == "Passed":
            passed_count += 1
        else:
            failed_count += 1

        if grade > highest_student["grade"]:
            highest_student = student

        if grade < lowest_student["grade"]:
            lowest_student = student

    number_of_students = len(students)
    average = total_grade / number_of_students if number_of_students > 0 else 0

    statistics = {
        "number_of_students": number_of_students,
        "average": average,
        "passed_count": passed_count,
        "failed_count": failed_count,
        "highest_student": highest_student,
        "lowest_student": lowest_student
    }

    return statistics


def display_students(students):
    print(f"\n{'Student No.':<12}{'Name':<20}{'Grade':<10}{'Classification':<20}{'Status':<10}")
    print("-" * 72)

    for student in students:
        classification, status = classify_grade(student["grade"])
        name = student["name"][:18]  
        print(f"{student['student_id']:<12}{name:<20}{student['grade']:<10.2f}"
              f"{classification:<20}{status:<10}")


def display_statistics(statistics):
    if not statistics:
        print("No statistics available.")
        return

    print("\nCLASS STATISTICS")
    print(f"Number of students: {statistics['number_of_students']}")
    print(f"Class average: {statistics['average']:.2f}")
    print(f"Passed: {statistics['passed_count']}")
    print(f"Failed: {statistics['failed_count']}")
    print(f"Highest: {statistics['highest_student']['name']} - "
          f"{statistics['highest_student']['grade']:.2f}")
    print(f"Lowest: {statistics['lowest_student']['name']} - "
          f"{statistics['lowest_student']['grade']:.2f}")


def search_student(students, keyword):
    matches = []

    keyword = keyword.strip().lower()

    for student in students:
        if keyword in student["student_id"].lower() or keyword in student["name"].lower():
            matches.append(student)

    return matches


def save_report(students, statistics, filename):
    try:
        with open(filename, "w") as file:
            file.write("STUDENT GRADE ANALYZER - REPORT\n")
            file.write("=" * 50 + "\n\n")

            file.write("STUDENT RESULTS\n")
            file.write("-" * 50 + "\n")
            for student in students:
                classification, status = classify_grade(student["grade"])
                file.write(
                    f"{student['student_id']} - {student['name']} - "
                    f"{student['grade']:.2f} - {classification} - {status}\n"
                )

            if statistics:
                file.write("\nCLASS STATISTICS\n")
                file.write("-" * 50 + "\n")
                file.write(f"Number of students: {statistics['number_of_students']}\n")
                file.write(f"Class average: {statistics['average']:.2f}\n")
                file.write(f"Passed: {statistics['passed_count']}\n")
                file.write(f"Failed: {statistics['failed_count']}\n")
                file.write(
                    f"Highest: {statistics['highest_student']['name']} - "
                    f"{statistics['highest_student']['grade']:.2f}\n"
                )
                file.write(
                    f"Lowest: {statistics['lowest_student']['name']} - "
                    f"{statistics['lowest_student']['grade']:.2f}\n"
                )

        print(f"Report successfully saved to '{filename}'.")

    except OSError as error:
        print(f"Error: Could not save the report. ({error})")


def main():
    students = load_students("grades.txt")

    if not students:
        print("No valid student records were loaded.")
        return

    statistics = calculate_statistics(students)

    while True:
        print("\nSTUDENT GRADE ANALYZER")
        print("[1] Display all students")
        print("[2] Display class statistics")
        print("[3] Search for a student")
        print("[4] Save report")
        print("[5] Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_students(students)
        elif choice == "2":
            display_statistics(statistics)
        elif choice == "3":
            keyword = input("Enter student number or name to search: ").strip()
            results = search_student(students, keyword)
            if results:
                display_students(results)
            else:
                print("No matching student found.")
        elif choice == "4":
            save_report(students, statistics, "grade_report.txt")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    main()
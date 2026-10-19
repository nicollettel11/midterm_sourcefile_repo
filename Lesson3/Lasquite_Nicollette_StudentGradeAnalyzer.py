# Store the raw comma-separated records.

raw_records = [
    "Ana,88,92,90",
    "Ben,70,72,74",
    "Cara,95,91,94",
    "Dan,78,80,76",
    "Ella,85,89,87",
    # adding some bad records here to test my guardian conditions
    "Fred,90,85",
    "Gina",
    "Henry,90,eighty,85",
    "Ivy,",
]

PASSING_GRADE = 75

# this dictionary will hold name -> list of scores
student_scores = {}

# PART A - go through each record, split it up, and store it properly
for record in raw_records:
    fields = record.split(",")

    # if it doesn't have exactly 4 parts (name + 3 scores), it's broken, skip it
    if len(fields) != 4:
        print(f"Skipped invalid record: {record}")
        continue

    name = fields[0]

    # try converting the scores to int, if one of them isn't a number just skip the whole record
    try:
        scores = [int(score) for score in fields[1:]]
    except ValueError:
        print(f"Skipped invalid record: {record}")
        continue

    student_scores[name] = scores


# PART B - just printing out what's in the dictionary so far, alphabetically
print("\nORGANIZED STUDENT RECORDS")
for name in sorted(student_scores.keys()):
    print(f"{name}: {student_scores[name]}")


ranking = []
passed_count = 0
failed_count = 0
sum_of_averages = 0

# PART C - now the actual math part, get avg/highest/lowest per student
for name, scores in student_scores.items():
    # just in case a student somehow has no scores at all, don't divide by 0
    if len(scores) == 0:
        continue

    total = sum(scores)
    average = total / len(scores)
    highest_score = max(scores)
    lowest_score = min(scores)

    # 75 is the cutoff so check against that
    if average >= PASSING_GRADE:
        remark = "Passed"
    else:
        remark = "Failed"

    if remark == "Passed":
        passed_count += 1
    else:
        failed_count += 1

    sum_of_averages += average

    # putting everything into one tuple, average first so sorting is easy later
    ranking.append((average, name, highest_score, lowest_score, remark))


# PART D - sort by average, highest first, then print the table
ranking.sort(reverse=True)

print("\nSTUDENT GRADE REPORT")
print("Rank  Name       Average  Highest  Lowest  Remark")

for rank, (average, name, highest_score, lowest_score, remark) in enumerate(ranking, start=1):
    print(f"{rank:<5} {name:<10} {average:<8.2f} {highest_score:<8} {lowest_score:<7} {remark}")


# PART E - wrap up with the class summary
num_students = len(ranking)

print("\nCLASS SUMMARY")
print(f"Number of Students: {num_students}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")

if num_students > 0:
    # since ranking is already sorted, top student is index 0, lowest is -1
    class_average = sum_of_averages / num_students
    highest_avg, highest_name, _, _, _ = ranking[0]
    lowest_avg, lowest_name, _, _, _ = ranking[-1]

    print(f"Class Average: {class_average:.2f}")
    print(f"Highest: {highest_name} - {highest_avg:.2f}")
    print(f"Lowest: {lowest_name} - {lowest_avg:.2f}")
else:
    # edge case, only matters if literally every record was invalid
    print("Class Average: N/A")
    print("Highest: N/A")
    print("Lowest: N/A")

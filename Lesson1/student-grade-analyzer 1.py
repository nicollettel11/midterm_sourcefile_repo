
scores = [85, 75, 96, 63, 71]


print("Student Scores:")
for score in scores:
    print(score)

print()

for i, score in enumerate(scores, start=1):
    if score >= 90:
        remark = "Excellent"
    elif score >= 80:
        remark = "Very Good"
    elif score >= 75:
        remark = "Good"
    else:
        remark = ""

    if score >= 75:
        print(f"Student {i}: {score} - {remark} - Passed")
    else:
        print(f"Student {i}: {score} - Failed")

print()


total = sum(scores)
average = total / len(scores)
highest = max(scores)
lowest = min(scores)


passed = sum(1 for s in scores if s >= 75)
failed = len(scores) - passed


print(f"Total Score: {total}")
print(f"Average Score: {average:.0f}")
print(f"Highest Score: {highest}")
print(f"Lowest Score: {lowest}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
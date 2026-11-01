marks = []

for i in range(5):
    m = float(input("Enter mark: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "F"

print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)
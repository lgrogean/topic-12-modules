import csv

total = 0
count = 0

with open("grades.csv", "r") as file:
     reader = csv.DictReader(file)
     report = []
     for row in reader:
         name = row["Name"]
         grade = int(row["Grade"])

         total += grade
         count += 1

         report.append(f"{name}: {grade}")

average = total / count

with open("report.txt", "w") as file:
    file.write("Student Grade Report\n")
    file.write("--------------------\n")

    for line in report:
        file.write(line + "\n")

    file.write(f"\nAverage Grade: {average:.2f}")

print("Report saved to report.txt")


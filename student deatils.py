import csv
import json
import time

students = [["Roll Number", "Name", "Branch", "Physics", "Chemistry", "Maths"],
            [15, "Arka Bhattacharya", "SOC", 94, 88, 85],
            [26, "Lakshay Soni", "SOES", 97, 85, 89],
            [43, "Lakshay Jain", "SOC", 93, 90, 87],
            [25, "Jay Nagda", "SOC", 95, 88, 96],
            [56, "Anant Sharan", "SOES", 93, 91, 84]]

with open("student_details.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)


def get_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


time.sleep(2)
processed_records = []

# Read CSV and calculate results
with open("student_details.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    print("Roll  Name                 Branch  Total  Percentage  Grade")
    for row in reader:
        roll = row[0]
        name = row[1]
        branch = row[2]
        marks = [int(m) for m in row[3:]]

        total = sum(marks)
        percentage = total / len(marks)
        grade = get_grade(percentage)

        print(roll.ljust(6), name.ljust(20), branch.ljust(7),
              str(total).ljust(6), str(round(percentage, 2)).ljust(11), grade)

        processed_records.append({"roll_number": int(roll),
                                  "name": name,
                                  "branch": branch,
                                  "total_marks": total,
                                  "percentage": round(percentage, 2),
                                  "grade": grade
                                  })
        print(f"Roll: {roll}, Name: {name}, Branch: {branch}, "
              f"Total: {total}, Percentage: {percentage:.2f}, Grade: {grade}")

time.sleep(2)
with open("students.json", "w") as f:
    json.dump(processed_records, f, indent=4)
print("\nProcessed records written to students.json")
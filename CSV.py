import csv
import time
import json

with open("students.csv", "w") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Roll Number", "SY"])
    writer.writerow(["Arka Bhattacharya", 15, 2])
    writer.writerow(["Lakshay Soni", 26, 1])
    writer.writerow(["Lakshay Jain", 43, 5])

time.sleep(2)
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['Name']}, Roll Number: {row['Roll Number']}, SY: {row['SY']}")

# time.sleep(2)
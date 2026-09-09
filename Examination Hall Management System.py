art2 = """----------- STUDENT INFORMATION -----------"""
art3 = """----------- SEATING ARRANGEMENT -----------"""

class student():
    def __init__(self, student_name, roll_no, hall_no, exam_block):
        self.student_name = student_name
        self.roll_no = roll_no
        self.hall_no = hall_no
        self.exam_block = exam_block

    def add_student(self):
        student_name = input("Enter Student Name: ")
        roll_no = int(input("Enter Roll No: "))
        hall_no = int(input("Enter Hall No: "))
        exam_block = input("Enter Exam block: ")

        self.student_name.append(student_name)
        self.roll_no.append(roll_no)
        self.hall_no.append(hall_no)
        self.exam_block.append(exam_block)

        print("\nStudent added successfully!\n")


class seating_information(student):
    def __init__(self, student_name, roll_no, hall_no, exam_block):
        super().__init__(student_name, roll_no, hall_no, exam_block)

    def show_information(self):
        print(f"\n{art2}\n")

        for i in range(len(self.student_name)):
            print(f"Name: {self.student_name[i]}\n"
                  f"Roll Number: {self.roll_no[i]}\n"
                  f"Hall Number: {self.hall_no[i]}\n"
                  f"Block: {self.exam_block[i]}")
            print("-------------------------------------------")


class seating_arrangement(student):
    def __init__(self, student_name, roll_no, hall_no, exam_block):
        super().__init__(student_name, roll_no, hall_no, exam_block)

    def show_arrangement(self):
        print(f"\n{art3}\n")

        blocks = sorted(set(self.exam_block))
        for block in blocks:
            print(f"Block {block}")
            print("--------------------------------")

            seat_no = 1
            found = False
            hall_printed = False
            for i in range(len(self.exam_block)):
                if self.exam_block[i] == block:
                    if not hall_printed:
                        print(f"Hall {self.hall_no[i]}")
                        hall_printed = True

                    print(f"Seat {seat_no} : {self.student_name[i]} ({self.roll_no[i]})")

                    seat_no += 1
                    found = True
            print("\n")
            if not found:
                print("No students assigned")
                print("\n")


class unique_paths:
    def calculate_paths(self):
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))

        dp = [[0] * columns for _ in range(rows)]

        for i in range(columns):
            dp[0][i] = 1

        for i in range(rows):
            dp[i][0] = 1

        for i in range(1, rows):
            for j in range(1, columns):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[rows - 1][columns - 1]

continue_program = True
menu = """========================================
     EXAMINATION HALL MANAGEMENT SYSTEM
========================================

1. Add Student
2. Display Student Information
3. Display Seating Arrangement
4. Unique Paths Problem
5. Exit"""

student_name = []
roll_no = []
hall_no = []
exam_block = []

Student = student(student_name, roll_no, hall_no, exam_block)
Seating_info = seating_information(student_name, roll_no, hall_no, exam_block)
Seating_arrangement = seating_arrangement(student_name, roll_no, hall_no, exam_block)
Unique_Paths = unique_paths()

while continue_program:
    print(f"{menu}\n")
    choice = input("Enter your choice: ").strip()
    print("\n")

    if choice == "1":
        Student.add_student()
    elif choice == "2":
        Seating_info.show_information()
    elif choice == "3":
        Seating_arrangement.show_arrangement()
    elif choice == "4":
        num_paths = Unique_Paths.calculate_paths()
        print(f"\nNumber of unique paths: {num_paths}\n")
    else:
        print("Thank you for using\nExamination Hall Management System\nProgram terminated")
        continue_program = False

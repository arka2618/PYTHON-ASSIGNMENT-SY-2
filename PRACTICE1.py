# Required arguments
def student(rollno, name):
    print(f"Student name: {name}, Roll no: {rollno}")
# student(15, "xyz")

# Keyword argument
def Student(name, rollno):
    print(f"I am {name}, roll no {rollno}")
# Student(name="Arka", rollno=15)

# Variable length argument
x = list(map(str, input("What subjects do you like: ").split(',')))
sub = []
for i in x:
    sub = sub.append(i)
    print(sub)
    print(f"I am good in subjects like {sub}")

# Default argument
def STUDENT(rollno, name, Class = "SY-2"):
    print(f"{name} of Class {Class}, Roll no {rollno}")
# STUDENT(rollno=15, name="Arka")
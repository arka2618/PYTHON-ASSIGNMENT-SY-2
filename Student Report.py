from datetime import datetime
from functools import wraps

class Report:
    def __init__(self, title, author, date, content):
        self.title = title
        self.author = author
        self.date = date
        self.content = content

    @classmethod
    def student_template(cls, author, content, date=None):
        date = date or datetime.now().strftime("%d/%m/%Y")
        return cls(title="Student Report", author=author, date=date, content=content)

    def __str__(self):
        return (f"{self.title}\nAuthor : {self.author}\nDate : {self.date}\n{self.content}")

    def __len__(self):
        return len(str(self))

    def __eq__(self, other):
        if not isinstance(other, Report):
            return NotImplemented
        return (self.title == other.title
                and self.author == other.author
                and self.content == other.content)

def add_border(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        border = "=" * 40
        return f"{border}\n{text}\n{border}"
    return wrapper

def uppercase(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

def add_footer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return f"{text}\nEnd of Report"
    return wrapper

@add_border
@add_footer
@uppercase
def generate_report(report: Report) -> str:
    return str(report)


if __name__ == "__main__":
    student_report = Report.student_template(author="Arka Bhattacharya", content="Enrollment No : ADT0210\nCGPA : 8.29")

    # __str__
    print("\n")
    print(student_report)

    # __len__
    print("\n")
    print(f"Report Length: {len(student_report)}")

    # same_report = Report.student_template(
    #     author="Sushma",
    #     content="Marks : 95\nGrade : A",
    #     date=student_report.date,
    # )
    # # __eq__
    # print(student_report == same_report)

    print("\n")
    print(generate_report(student_report))
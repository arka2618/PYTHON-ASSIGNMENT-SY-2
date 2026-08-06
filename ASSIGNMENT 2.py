from datetime import datetime
from functools import wraps

class Report:
    def __init__(self, title, author, date, fields):
        self.title = title
        self.author = author
        self.date = date
        self.fields = fields

    @classmethod
    def _build(cls, title, author, fields, date=None):
        date = date or datetime.now().strftime("%d/%m/%Y")
        return cls(title=title, author=author, date=date, fields=fields)

    @classmethod
    def student_template(cls, author, student_name, roll_no, cgpa, date=None):
        fields = {"Student Name": student_name, "Roll no": roll_no, "CGPA": cgpa}
        return cls._build("Student Report", author, fields, date)

    @classmethod
    def employee_template(cls, author, employee_name, department, salary, date=None):
        fields = {"Employee Name": employee_name, "Department": department, "Salary": salary}
        return cls._build("Employee Report", author, fields, date)

    @classmethod
    def sales_template(cls, author, product, quantity, revenue, date=None):
        fields = {"Product": product, "Quantity": quantity, "Revenue": revenue}
        return cls._build("Sales Report", author, fields, date)

    @classmethod
    def attendance_template(cls, author, student_name, total_classes, attended, percentage, date=None):
        fields = {"Student Name": student_name,
                  "Total Classes": total_classes,
                  "Attended": attended,
                  "Percentage": percentage
                  }
        return cls._build("Attendance Report", author, fields, date)

    @classmethod
    def inventory_template(cls, author, item_name, quantity_in_stock, unit_price, date=None):
        fields = {"Item Name": item_name,
                  "Quantity in Stock": quantity_in_stock,
                  "Unit Price": unit_price
                  }
        return cls._build("Inventory Report", author, fields, date)

    def _fields_as_text(self):
        return "\n".join(f"{name} : {value}" for name, value in self.fields.items())

    def __str__(self):
        return (f"{self.title}\nAuthor : {self.author}\nDate : {self.date}\n{self._fields_as_text()}")

    def __len__(self):
        return len(str(self))

    def __eq__(self, other):
        if not isinstance(other, Report):
            return NotImplemented
        return (self.title == other.title
                and self.author == other.author
                and self.fields == other.fields)

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
    reports = [Report.student_template(author="Vishal Bharadwaj", student_name="Arka Bhattacharya", roll_no=15, cgpa=8.29),
               Report.employee_template(author="Vishal Bharadwaj", employee_name="Dharmendra Pradhan", department="Engineering", salary=75000),
               Report.sales_template(author="Vishal Bharadwaj", product="Laptop", quantity=12, revenue=960000),
               Report.attendance_template(author="Vishal Bharadwaj", student_name="Arka Bhattacharya", total_classes=60, attended=54, percentage="90%"),
               Report.inventory_template(author="Vishal Bharadwaj", item_name="Wireless Mouse", quantity_in_stock=230, unit_price=450)]

    for report in reports:
        print(generate_report(report))
        print("\n")
        print(f"[length: {len(report)} characters]\n")

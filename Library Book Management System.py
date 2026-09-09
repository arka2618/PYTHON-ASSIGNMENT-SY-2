art1 = """----------- BOOK INFORMATION -----------"""
art2 = """----------- ALL BOOKS IN LIBRARY -----------"""

class book():
    def __init__(self, book_title, author_name, price, category):
        self.book_title = book_title
        self.author_name = author_name
        self.price = price
        self.category = category

    def add_book(self):
        book_title = input("Enter Book Title: ")
        author_name = input("Enter Author Nmae: ")
        price = float(input("Enter Price: ₹"))

        self.book_title.append(book_title)
        self.author_name.append(author_name)
        self.price.append(price)
        print("\nBook added successfully!\n")

    def check_category(self):
        if self.price[-1] < 500:
            self.category.append("Basic")
        elif self.price[-1] >= 500 and self.price[-1] <= 999:
            self.category.append("Standard")
        elif self.price[-1] >= 1000:
            self.category.append("Premium")


class book_information(book):
    def __init__(self, book_title, author_name, price, category):
        super().__init__(book_title, author_name, price, category)

    def show_information(self):
        print(f"\n{art1}\n")

        for i in range(len(self.book_title)):
            print(f"Book Title  : {self.book_title[i]}\n"
                  f"Author Name : {self.author_name[i]}\n"
                  f"Price       : ₹{self.price[i]}\n"
                  f"Category.   : {self.category[i]}")
            print("-------------------------------------------")


class library_information(book):
    def __init__(self, book_title, author_name, price, category):
        super().__init__(book_title, author_name, price, category)

    def show_library(self):
        print(f"\n{art2}\n")

        num = 1
        for i in range(len(self.book_title)):
            print(f"{num}. {self.book_title[i]}\n"
                  f"   Author   : {self.author_name[i]}\n"
                  f"   Price    : ₹{self.price[i]}\n"
                  f"   Category : {self.category[i]}")
            num += 1
            print("\n")


class climbing_stairs:
    def count_ways(self, n):
        dp = [0] * (n + 1)

        # Base cases
        dp[0] = 1
        if n >= 1:
            dp[1] = 1
        # Fill DP table
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        print("\nDynamic Programming Table:")
        for i in range(n + 1):
            print(f"Stair {i} : {dp[i]}")

        print(f"\nNumber of ways to climb {n} stairs: {dp[n]}")

continue_program = True
menu = """
========================================
      LIBRARY BOOK MANAGEMENT SYSTEM
========================================

1. Add Book
2. Display Book Information
3. Display All Books
4. Climbing Stairs Problem
5. Exit"""

book_title = []
author_name = []
price = []
category = []

Book = book(book_title, author_name, price, category)
Book_info = book_information(book_title, author_name, price, category)
Library_info = library_information(book_title, author_name, price, category)
ClimbingStairs = climbing_stairs()

while continue_program:
    print(f"\n{menu}\n")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        Book.add_book()
        Book.check_category()
    elif choice == "2":
        Book_info.show_information()
    elif choice == "3":
        Library_info.show_library()
    elif choice == "4":
        n = int(input("Enter number of stairs: "))
        ClimbingStairs.count_ways(n)
    else:
        print("Thank you for using\nLibrary Book Management System\nProgram terminated")
        continue_program = False

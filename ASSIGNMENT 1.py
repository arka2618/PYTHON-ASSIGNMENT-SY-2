class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = True

    def book_available(self):
        status = "Available" if self.is_available else "Not Available"
        print(f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Status: {status}")

class Patron:
    def __init__(self, patron_id, name, age):
        self.patron_id = patron_id
        self.name = name
        self.age = age
        self.borrowed_book = []

    def borrow_book(self, book):
        if book.is_available:
            self.borrowed_book.append(book)
            book.is_available = False

    def return_book(self, book):
        if book in self.borrowed_book:
            self.borrowed_book.remove(book)
            book.is_available = True

class Library:
    def __init__(self, books, patrons):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book {book.title} added to the library")

    def add_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron {patron.name} has been successfully registered")

    def borrow_book(self, patron_id, book_id):
        patron = self.patrons[patron_id]
        book = self.books[book_id]

        if patron_id not in self.patrons:
            print(f"Patron with ID {patron_id} is not registered")
            return
        if book_id not in self.books:
            print(f"Book with ID {book_id} is not available in the library")
            return
        if book.is_available == False:
            print(f"Book {book.title} is currently not available")
        else:
            print(f"Book {book.title} is available")

# x = Book("LIB01", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
# x.book_available()

# y = Patron("P01", "John Doe", 30)
# y.borrow_book(x)
# y.borrowed_book[0].book_available()
# y.return_book(x)

# z = Library({}, {})
# z.add_book(x)
# z.add_patron(y)
# z.borrow_book("P01", "LIB01")
# z.borrow_book("P01", "LIB01")  # Attempt to borrow the same book again

class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre
        self.is_available = True

    def display(self):
        status = "Available" if self.is_available else "Not Available"
        print(f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Status: {status}")

class Patron:
    def __init__(self, patron_id, name, age):
        self.patron_id = patron_id
        self.name = name
        self.age = age
        self.borrowed_book = []

    def borrow_book(self, book):
        self.borrowed_book.append(book)
        book.is_available = False

    def return_book(self, book):
        self.borrowed_book.remove(book)
        book.is_available = True

    def display(self):
        titles = [b.title for b in self.borrowed_books]
        print(f"Patron ID: {self.patron_id}, Name: {self.name}, Age: {self.age}, Borrowed: {titles if titles else 'None'}")

class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book {book.title} added to the library")

    def add_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron {patron.name} has been successfully registered")

    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print(f"Patron with ID {patron_id} is not registered")
            return
        if book_id not in self.books:
            print(f"Book with ID {book_id} is not available in the library")
            return

        patron = self.patrons[patron_id]
        book = self.books[book_id]
        
        if  not book.is_available:
            print(f"Book {book.title} is currently not available")
            return
        patron.borrow_book(book)
        print(f"{book.title} borrowed successfully by {patron.name}")

    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print(f"Patron with ID {patron_id} is not registered")
            return
        if book_id not in self.books:
            print(f"Book with ID {book_id} does not exist")
            return

        patron = self.patrons[patron_id]
        book = self.books[book_id]

        if book not in patron.borrowed_books:
            print(f"{patron.name} did not borrow {book.title}")
            return
        
        patron.return_book(book)
        print(f"{book.title} returned successfully by {patron.name}")

        def list_books(self):
            if not self.books:
                print("No books in the library")
            for book in self.books.values():
                book.display()

        def list_patrons(self):
            if not self.patrons:
                print("No patrons registered")
            for patron in self.patrons.values():
                patron.display()


library = Library()
menu = """1. Add a book
2. Register a patron
3. Borrow a book
4. Return a book
5. List all books
6. List all patrons
7. Exit"""
continue_operation = True

while continue_operation:
        print(menu)
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            book_id = input("Book ID: ").strip()
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            genre = input("Genre: ").strip()
            library.add_book(Book(book_id, title, author, genre))

        elif choice == "2":
            patron_id = input("Patron ID: ").strip()
            name = input("Name: ").strip()
            age = input("Age: ").strip()
            library.add_patron(Patron(patron_id, name, age))

        elif choice == "3":
            patron_id = input("Patron ID: ").strip()
            book_id = input("Book ID: ").strip()
            library.borrow_book(patron_id, book_id)

        elif choice == "4":
            patron_id = input("Patron ID: ").strip()
            book_id = input("Book ID: ").strip()
            library.return_book(patron_id, book_id)

        elif choice == "5":
            library.list_books()

        elif choice == "6":
            library.list_patrons()

        elif choice == "7":
            print("Exiting library system. Goodbye.")
            break
        else:
            print("Invalid option, choose a number between 1 and 7")

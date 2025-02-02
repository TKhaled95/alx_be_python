# Base class - Book
class Book:
    def __init__(self, title, author):
        """Initialize Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of a Book."""
        return f"Book: {self.title} by {self.author}"


# Derived class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize EBook with title, author, and file_size."""
        super().__init__(title, author)  # Call the parent class constructor
        self.file_size = file_size

    def __str__(self):
        """String representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize PrintBook with title, author, and page_count."""
        super().__init__(title, author)  # Call the parent class constructor
        self.page_count = page_count

    def __str__(self):
        """String representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition class - Library
class Library:
    def __init__(self):
        """Initialize Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a Book (or derived type) to the library."""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library."""
        for book in self.books:
            print(book)


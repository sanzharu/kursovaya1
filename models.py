class Book:
    def __init__(self, title, author, genre, year, isbn):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.isbn = isbn

class Author:
    def __init__(self, name, birth_year, country):
        self.name = name
        self.birth_year = birth_year
        self.country = country

class Reader:
    def __init__(self, name, reader_id, email, phone):
        self.name = name
        self.reader_id = reader_id
        self.email = email
        self.phone = phone

class LibraryCard:
    def __init__(self, reader, issue_date, expiration_date):
        self.reader = reader
        self.issue_date = issue_date
        self.expiration_date = expiration_date

class Librarian:
    def __init__(self, name, librarian_id, email, phone, schedule):
        self.name = name
        self.librarian_id = librarian_id
        self.email = email
        self.phone = phone
        self.schedule = schedule

class BorrowRecord:
    def __init__(self, book, reader, librarian, borrow_date, return_date=None):
        self.book = book
        self.reader = reader
        self.librarian = librarian
        self.borrow_date = borrow_date
        self.return_date = return_date

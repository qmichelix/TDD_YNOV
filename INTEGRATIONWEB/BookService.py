# INTEGRATIONWEB/BookService.py

class BookService:
    def __init__(self):
        self.books_db = []

    def get_books(self):
        return self.books_db

    def add_book(self, book):
        self.books_db.append(book)

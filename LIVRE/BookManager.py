from LIVRE.Book import Book

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added")
        # Ajoutez ici une logique pour vérifier les doublons si nécessaire
        self.books.append(book)

    def list_books(self):
        return sorted(self.books, key=lambda book: book.title)

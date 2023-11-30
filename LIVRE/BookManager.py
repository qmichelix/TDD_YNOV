from LIVRE.Book import Book

# Classe pour gérer la liste des livres
class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        # Vérifie si l'objet ajouté est une instance de Book
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added")
        self.books.append(book)

    def list_books(self):
        # Retourne la liste des livres triée par titre
        return sorted(self.books, key=lambda book: book.title)

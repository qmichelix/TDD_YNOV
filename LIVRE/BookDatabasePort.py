from LIVRE.Book import Book
from LIVRE.BookManager import BookManager

from abc import ABC, abstractmethod

# Interface abstraite pour la base de données des livres
class BookDatabasePort(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def get_all_books(self):
        pass

# Implémentation concrète de l'interface pour la base de données
class BookDatabaseImplementation(BookDatabasePort):
    def __init__(self):
        # Initialisation de la connexion à la base de données
        pass

    def add_book(self, book):
        # Logique pour ajouter un livre à la base de données
        pass

    def get_all_books(self):
        # Logique pour récupérer tous les livres de la base de données
        pass

# Modification de la classe BookManager pour utiliser le port de base de données
class BookManager:
    def __init__(self, db_port: BookDatabasePort):
        self.db_port = db_port
        self.books = []

    def add_book(self, book):
        self.db_port.add_book(book)
        self.books.append(book)

    def list_books(self):
        return sorted(self.books, key=lambda book: book.title)

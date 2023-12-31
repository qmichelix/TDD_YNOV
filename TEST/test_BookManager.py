from LIVRE.Book import Book
from LIVRE.BookManager import BookManager
import pytest

# Tests pour BookManager

def test_add_book():
    # Test l'ajout d'un livre au gestionnaire
    manager = BookManager()
    book = Book("Harry Potter", "JK Rowling")
    manager.add_book(book)
    assert book in manager.books

def test_list_books_in_alphabetical_order():
    # Test si les livres sont listés dans l'ordre alphabétique
    manager = BookManager()
    book1 = Book("Animal Farm", "George Orwell")
    book2 = Book("1984", "George Orwell")
    manager.add_book(book1)
    manager.add_book(book2)
    assert manager.list_books() == [book2, book1]

def test_list_books_contains_all_books():
    # Test si la liste des livres contient tous les livres ajoutés
    manager = BookManager()
    book1 = Book("Animal Farm", "George Orwell")
    book2 = Book("1984", "George Orwell")
    book3 = Book("Harry Potter", "JK Rowling")
    manager.add_book(book1)
    manager.add_book(book2)
    manager.add_book(book3)
    assert set(manager.list_books()) == {book1, book2, book3}

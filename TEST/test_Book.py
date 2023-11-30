from LIVRE.Book import Book
import pytest
# Tests pour la classe Book

def test_create_book_with_valid_data():
    # Test la création d'un livre avec des données valides
    book = Book("Harry Potter", "JK Rowling")
    assert book.title == "Harry Potter"
    assert book.author == "JK Rowling"

def test_create_book_with_empty_title_raises_error():
    # Test la levée d'une erreur si le titre est vide
    with pytest.raises(ValueError):
        Book("", "JK Rowling")

def test_create_book_with_empty_author_raises_error():
    # Test la levée d'une erreur si l'auteur est vide
    with pytest.raises(ValueError):
        Book("Harry Potter", "")

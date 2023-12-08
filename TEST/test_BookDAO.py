import pytest
from LIVRE.BookDAO import BookDAO
from LIVRE.Book import Book

@pytest.fixture(scope="module")
def book_dao():
    db_url = "postgresql://user:password@localhost:5432/test_db"
    return BookDAO(db_url)

def test_add_book(book_dao):
    book = Book("Test Title", "Test Author")
    book_dao.add_book(book)

    # Récupérer tous les livres et vérifier si un livre avec le même titre et auteur existe
    all_books = book_dao.get_all_books()
    assert any(b.title == "Test Title" and b.author == "Test Author" for b in all_books)

def test_get_all_books(book_dao):
    books = book_dao.get_all_books()
    # Vérifiez la liste des livres
    assert isinstance(books, list)

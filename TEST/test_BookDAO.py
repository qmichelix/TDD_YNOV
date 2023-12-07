import pytest
from LIVRE.BookDAO import BookDAO
from LIVRE.Book import Book

@pytest.fixture(scope="module")
def book_dao():
    # Initialisez ici votre DAO, par exemple avec une connexion à la base de données
    return BookDAO()

def test_add_book(book_dao):
    book = Book("Test Title", "Test Author")
    book_dao.add_book(book)
    # Ajoutez ici des assertions pour vérifier que le livre a été ajouté

def test_get_all_books(book_dao):
    books = book_dao.get_all_books()
    # Ajoutez ici des assertions pour vérifier la liste des livres

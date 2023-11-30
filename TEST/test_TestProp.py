from LIVRE.Book import Book
from LIVRE.BookManager import BookManager
import pytest
import pytest
from LIVRE.BookManager import BookManager

@pytest.fixture
def book_manager():
    return BookManager()

# Importation de la bibliothèque Hypothesis
from hypothesis import given, strategies as st

def test_book_list_contains_all_books(book_manager):
    @given(st.lists(st.builds(Book, title=st.text(min_size=1), author=st.text(min_size=1)), unique=True))
    def property_test(books):
        for book in books:
            book_manager.add_book(book)
        assert sorted(book_manager.list_books(), key=lambda book: book.title) == sorted(books, key=lambda book: book.title)
    property_test()


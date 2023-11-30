import pytest

from hypothesis import given, strategies as st, settings, HealthCheck
from LIVRE.Book import Book
from LIVRE.BookManager import BookManager

# Pas besoin de modifier la fixture ici
@pytest.fixture
def book_manager():
    return BookManager()

# Utilisation de deux décorateurs : `given` et `settings`
@given(st.lists(st.builds(Book, title=st.text(min_size=1), author=st.text(min_size=1)), unique=True))
@settings(suppress_health_check=[HealthCheck.function_scoped_fixture])
def test_book_list_contains_all_books(book_manager, books):
    for book in books:
        book_manager.add_book(book)
    assert sorted(book_manager.list_books(), key=lambda book: book.title) == sorted(books, key=lambda book: book.title)

from LIVRE.Book import Book
from LIVRE.BookManager import BookManager
import pytest
from hypothesis import HealthCheck, given, strategies as st

@given(st.lists(st.builds(Book, title=st.text(min_size=1), author=st.text(min_size=1)), unique=True), 
       settings=st.settings(suppress_health_check=[HealthCheck.function_scoped_fixture]))
def test_book_list_contains_all_books(book_manager, books):
    for book in books:
        book_manager.add_book(book)
    assert sorted(book_manager.list_books(), key=lambda book: book.title) == sorted(books, key=lambda book: book.title)

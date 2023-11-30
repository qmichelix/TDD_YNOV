from hypothesis import given, strategies as st
from LIVRE.Book import Book
from LIVRE.BookManager import BookManager

@given(st.lists(st.builds(Book, st.text(min_size=1), st.text(min_size=1))))
def test_list_books_contains_all_generated_books(books):
    manager = BookManager()
    for book in books:
        manager.add_book(book)
    assert set(manager.list_books()) == set(books)

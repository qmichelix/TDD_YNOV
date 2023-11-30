from LIVRE.Book import Book
from LIVRE.BookManager import BookManager
import pytest
# Importation de la bibliothèque Hypothesis
from hypothesis import given, strategies as st

# Test de propriété pour vérifier que la liste des livres retournés contient tous les éléments de la liste stockée
def test_book_list_contains_all_books(book_manager):
    @given(st.lists(st.builds(Book, title=st.text(), author=st.text())))
    def property_test(books):
        for book in books:
            book_manager.add_book(book)
        assert set(book_manager.list_books()) == set(books)
    property_test()

import pytest
from flask_testing import TestCase
from INTEGRATIONWEB.Controller import app
from LIVRE.BookManager import BookManager
from LIVRE.Book import Book

class TestBookApi(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_books(self, mocker):
        # Mock the BookManager's list_books method
        mocker.patch.object(BookManager, 'list_books', return_value=[Book("Test Book", "Test Author")])

        response = self.client.get('/books')
        assert response.status_code == 200
        assert response.json == [{"title": "Test Book", "author": "Test Author"}]

    def test_add_book(self, mocker):
        # Mock the BookManager's add_book method
        mocker.patch.object(BookManager, 'add_book')

        book_data = {"title": "New Book", "author": "New Author"}
        response = self.client.post('/books', json=book_data)
        assert response.status_code == 201
        assert response.json == book_data

        # Verify if the add_book method was called
        BookManager.add_book.assert_called_once_with(Book("New Book", "New Author"))

    def test_error_handling(self):
        # Test error handling for bad request
        response = self.client.post('/books', json={"title": "Incomplete Data"})
        assert response.status_code == 400

# Run the tests
if __name__ == '__main__':
    pytest.main()

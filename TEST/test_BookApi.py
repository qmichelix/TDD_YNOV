import pytest
from flask.testing import FlaskClient
from unittest.mock import patch
from INTEGRATIONWEB.Controller import app
from INTEGRATIONWEB.DTO import BookDTO

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_books_with_mock(client):
    with patch('INTEGRATIONWEB.Controller.book_service') as mock_service:
        mock_service.get_books.return_value = [BookDTO("Mock Book", "Mock Author")]
        response = client.get('/books')
        assert response.status_code == 200
        assert response.json == [{"title": "Mock Book", "author": "Mock Author"}]

def test_add_book_with_mock(client):
    book = {"title": "Test Book", "author": "Test Author"}
    with patch('INTEGRATIONWEB.Controller.book_service') as mock_service:
        response = client.post('/books', json=book)
        assert response.status_code == 201
        mock_service.add_book.assert_called_once()

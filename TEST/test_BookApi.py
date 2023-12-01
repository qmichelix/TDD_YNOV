import pytest
from flask.testing import FlaskClient
from unittest.mock import patch
from INTEGRATIONWEB.Controller import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_books_with_mock(client):
    with patch('INTEGRATIONWEB.Controller.BookService') as mock_service:
        mock_service.get_books.return_value = [BookDTO("Mock Book", "Mock Author")]
        response = client.get('/books')
        assert response.status_code == 200
        assert response.json == [{"title": "Mock Book", "author": "Mock Author"}]

def test_error_handling_with_mock(client):
    with patch('INTEGRATIONWEB.Controller.BookService') as mock_service:
        mock_service.add_book.side_effect = Exception("Error")
        response = client.post('/books', json={"title": "Test Book", "author": "Test Author"})
        assert response.status_code == 500  # or whatever your error handling logic is

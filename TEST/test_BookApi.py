import pytest
from flask import Flask
from INTEGRATIONWEB.Controller import app as flask_app
from INTEGRATIONWEB.BookService import BookService

@pytest.fixture
def app():
    app = flask_app
    app.config['TESTING'] = True
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_books(client, mocker):
    mock_service = mocker.patch.object(BookService, 'get_books', return_value=[])
    response = client.get('/books')
    assert response.status_code == 200
    mock_service.assert_called_once()

def test_add_book(client, mocker):
    book_data = {"title": "Test Book", "author": "Test Author"}
    mock_service = mocker.patch.object(BookService, 'add_book', return_value=book_data)
    response = client.post('/books', json=book_data)
    assert response.status_code == 201
    mock_service.assert_called_once_with(book_data)

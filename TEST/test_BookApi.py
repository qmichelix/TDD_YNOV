import pytest
from flask.testing import FlaskClient
from INTEGRATIONWEB.Controller import app
from INTEGRATIONWEB.DTO import BookDTO

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_add_book(client):
    book = {"title": "Test Book", "author": "Test Author"}
    response = client.post('/books', json=book)
    assert response.status_code == 201
    assert response.json == book

    # Verify if the book is added
    get_response = client.get('/books')
    assert book in get_response.json

def test_error_handling(client):
    # Test error handling for bad request
    response = client.post('/books', json={"title": "Incomplete Data"})
    assert response.status_code == 400

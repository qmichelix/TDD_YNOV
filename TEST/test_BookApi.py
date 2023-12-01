import pytest
from INTEGRATIONWEB.Dto import BookDTO
from INTEGRATIONWEB.Controller import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_books(client, mocker):
    # Simuler une méthode de service
    mock_service = mocker.patch('INTEGRATIONWEB.YourService.your_service_function', return_value=[{"title": "Mock Book", "author": "Mock Author"}])

    response = client.get('/books')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    # Vérifier si le mock a été appelé
    mock_service.assert_called_once()

def test_add_book(client, mocker):
    # Simuler une méthode de service, si nécessaire
    book = {"title": "Test Book", "author": "Test Author"}
    response = client.post('/books', json=book)
    assert response.status_code == 201
    assert response.json == book

    # Vérifier si le livre est ajouté
    get_response = client.get('/books')
    assert book in get_response.json

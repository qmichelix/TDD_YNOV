import pytest
from flask_testing import TestCase
from INTEGRATIONWEB.Dto import BookDTO
from INTEGRATIONWEB.Controller import app
# Importez le service ou la fonction que vous voulez mocker
# from INTEGRATIONWEB.YourService import your_service_function

class TestBookApi(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_books(self, mocker):
        # Simuler une méthode de service
        mock_service = mocker.patch('INTEGRATIONWEB.YourService.your_service_function', return_value=[{"title": "Mock Book", "author": "Mock Author"}])

        response = self.client.get('/books')
        assert response.status_code == 200
        assert isinstance(response.json, list)
        # Vous pouvez également vérifier si le mock a été appelé
        mock_service.assert_called_once()

    def test_add_book(self, mocker):
        # Simuler une méthode de service, si nécessaire
        book = {"title": "Test Book", "author": "Test Author"}
        response = self.client.post('/books', json=book)
        assert response.status_code == 201
        assert response.json == book

        # Vérifier si le livre est ajouté
        get_response = self.client.get('/books')
        assert book in get_response.json

import pytest
from flask_testing import TestCase
from INTEGRATIONWEB.Dto import BookDTO
from INTEGRATIONWEB.Controller import app


class TestBookApi(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_books(self):
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_add_book(self):
        book = {"title": "Test Book", "author": "Test Author"}
        response = self.client.post('/books', json=book)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, book)

        # Verify if the book is added
        get_response = self.client.get('/books')
        self.assertIn(book, get_response.json)

if __name__ == '__main__':
    pytest.main()

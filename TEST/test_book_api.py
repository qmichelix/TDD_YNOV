from flask_testing import TestCase
from myapp import create_app, db
from myapp.models import Book

class TestBookAPI(TestCase):
    def create_app(self):
        # Configuration de l'application pour les tests
        return create_app('testing')

    def setUp(self):
        # Initialisation de la base de données de test
        db.create_all()

    def tearDown(self):
        # Nettoyage après les tests
        db.session.remove()
        db.drop_all()

    def test_get_books(self):
        # Test de la route GET
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)

    def test_post_book(self):
        # Test de la route POST
        response = self.client.post('/books', json={'title': 'New Book', 'author': 'Author'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.query.count(), 1)

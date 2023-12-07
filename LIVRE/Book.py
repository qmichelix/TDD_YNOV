# Import de pytest pour les tests
import pytest

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = 'books'  # Nom de la table dans la base de données

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def __init__(self, title, author):
        if not title or not author:
            raise ValueError("Title and author cannot be empty")
        self.title = title
        self.author = author

    def __repr__(self):
        return f"<Book(title='{self.title}', author='{self.author}')>"

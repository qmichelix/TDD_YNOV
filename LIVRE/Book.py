# Import de pytest pour les tests
import pytest

# Définition de la classe Book
class Book:
    def __init__(self, title, author):
        if not title or not author:
            raise ValueError("Title and author cannot be empty")
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

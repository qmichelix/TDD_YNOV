from flask import Flask, request, jsonify
from INTEGRATIONWEB.BookService import BookService

app = Flask(__name__)
book_service = BookService()

@app.route('/books', methods=['GET'])
def get_books():
    books = book_service.get_books()
    return jsonify([book.to_dict() for book in books])

@app.route('/books', methods=['POST'])
def add_book():
    book_data = request.json
    book = book_service.add_book(book_data)
    return jsonify(book.to_dict()), 201

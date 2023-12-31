from flask import Flask, request, jsonify
from INTEGRATIONWEB.DTO import BookDTO
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
    book = BookDTO.from_dict(book_data)
    book_service.add_book(book)
    return jsonify(book.to_dict()), 201

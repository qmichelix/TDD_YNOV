from flask import Flask, request, jsonify
from INTEGRATIONWEB.DTO import BookDTO
from LIVRE.BookManager import BookManager

app = Flask(__name__)

# Simulated database for demonstration
books_db = []

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify([book.to_dict() for book in books_db])

@app.route('/books', methods=['POST'])
def add_book():
    book_data = request.json
    book = BookDTO.from_dict(book_data)
    books_db.append(book)
    return jsonify(book.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)

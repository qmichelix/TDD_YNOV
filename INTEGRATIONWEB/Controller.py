from flask import Flask, request, jsonify
from LIVRE.Book import Book
from LIVRE.BookDAO import BookDAO

app = Flask(__name__)
book_dao = BookDAO()  # Assurez-vous que BookDAO est correctement initialisé

@app.route('/books', methods=['GET'])
def get_books():
    try:
        books = book_dao.get_all_books()
        return jsonify([book.to_dict() for book in books]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/books', methods=['POST'])
def add_book():
    book_data = request.json
    if 'title' not in book_data or 'author' not in book_data:
        return jsonify({"error": "Missing title or author"}), 400

    try:
        book = Book(title=book_data['title'], author=book_data['author'])
        book_dao.add_book(book)
        return jsonify(book.to_dict()), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

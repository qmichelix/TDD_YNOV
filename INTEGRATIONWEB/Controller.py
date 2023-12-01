from flask import Flask, request, jsonify
from INTEGRATIONWEB.DTO import BookDTO

app = Flask(__name__)

# Simulated database for demonstration
books_db = []

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify([book.to_dict() for book in books_db])

@app.route('/books', methods=['POST'])
def add_book():
    book_data = request.json
    # Vérifiez si toutes les données nécessaires sont présentes
    if 'title' not in book_data or 'author' not in book_data:
        return jsonify({"error": "Missing data"}), 400
    try:
        book = BookDTO.from_dict(book_data)
        books_db.append(book)
        return jsonify(book.to_dict()), 201
    except KeyError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

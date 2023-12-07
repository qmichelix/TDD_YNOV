from LIVRE.BookDAO import BookDAO

app = Flask(__name__)
book_service = BookService()

@app.route('/books', methods=['GET'])
def get_books():
    books = BookDAO.get_all_books()
    return jsonify([book.to_dict() for book in books])

@app.route('/books', methods=['POST'])
def add_book():
    book_data = request.json
    book = Book(title=book_data['title'], author=book_data['author'])
    BookDAO.add_book(book)
    return jsonify(book.to_dict()), 201

from flask import Flask, request, jsonify
from DTO import BookDTO

app = Flask(__name__)

# Route GET pour récupérer la liste des livres
@app.route('/books', methods=['GET'])
def get_books():
    # Ici, vous récupérerez la liste des livres de votre couche métier
    # Pour l'exemple, on retourne une liste vide
    books = []
    return jsonify([book.to_dict() for book in books])

# Route POST pour créer un nouveau livre
@app.route('/books', methods=['POST'])
def create_book():
    data = request.json
    book_dto = BookDTO.from_dict(data)
    # Ici, vous ajouterez le livre à votre couche métier
    # Pour l'exemple, on retourne simplement le DTO
    return jsonify(book_dto.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)

class BookDAO:
    def __init__(self, db):
        self.db = db

    def add_book(self, book):
        self.db.session.add(book)
        self.db.session.commit()

    def get_all_books(self):
        return Book.query.all()

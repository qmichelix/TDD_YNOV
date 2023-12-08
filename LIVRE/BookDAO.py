from LIVRE.Book import Book
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class BookDAO:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def add_book(self, book):
        with self.Session() as session:
            session.add(book)
            session.commit()

    def get_all_books(self):
        session = self.Session()
        try:
            return session.query(Book).all()
        finally:
            session.close()

    @staticmethod
    def _book_to_dict(book):
        return {
            'id': book.id,
            'title': book.title,
            'author': book.author
        }

from LIVRE.Book import Book
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class BookDAO:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def add_book(self, book):
        session = self.Session()
        session.add(book)
        session.commit()

    def get_all_books(self):
        session = self.Session()
        return session.query(Book).all()

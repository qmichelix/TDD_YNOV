class BookDTO:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author
        }

    @staticmethod
    def from_dict(data):
        return BookDTO(data['title'], data['author'])

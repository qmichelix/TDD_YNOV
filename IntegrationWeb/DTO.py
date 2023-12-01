class BookDTO:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def to_dict(self):
        """ Convertit l'objet DTO en dictionnaire pour faciliter la sérialisation JSON. """
        return {
            "title": self.title,
            "author": self.author
        }

    @staticmethod
    def from_dict(data):
        """ Crée un objet DTO à partir d'un dictionnaire. """
        return BookDTO(title=data["title"], author=data["author"])


class User():

    _is_librarian = False
    borrowed_books = []
    reserved_books = []

    def __init__(self, name):
        self.name = name

    def is_librarian(self):
        return self._is_librarian


class Librarian(User):

    _is_librarian = True

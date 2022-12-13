import logging
from script import populate

logging.basicConfig(level=logging.INFO)


class Shelf():
    def __init__(self):
        self.books = []

    def show_catalog(self):
        return self.books

    def add_book(self, user, book):
        if not user.is_librarian():
            logging.info(f'{user.name} cannot add books!')
            return False
        self.books.append(book)
        return True

    def remove_book(self, user, index):
        if not user.is_librarian():
            logging.info(f'{user.name} cannot remove books!')
            return False
        removed_book = self.books.pop(index)
        logging.info(f'{removed_book.name} has been removed from shelf!')
        return True
 
    def get_books_count(self):
        return len(self.books)

    def populate_book(self, file_name):
        populate(self, file_name)
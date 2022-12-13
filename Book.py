import logging
logging.basicConfig(level=logging.INFO)


class Book():
    def __init__(self, name, author, isbn):
        self.name = name
        self.author = author
        self.isbn = isbn

        self.borrowed_by = None
        self.reserved_by = None

    def borrow_book(self, user):
        if self.reserved_by and not self.reserved_by == user:
            logging.debug(f'{self.name} is already reserved')
            return False

        if self.borrowed_by:
            logging.debug(f'{self.name} is already borrowed')
            return False

        if self.reserved_by:
            for i in range(len(user.reserved_books)):
                if self.isbn == user.reserved_books[i].isbn:
                    user.reserved_books.pop(i)
                    break

        self.borrowed_by = user
        self.reserved_by = None
        user.borrowed_books.append(self)
        logging.info(f'{self.name} has been borrowed by {user.name}')
        return True

    def return_book(self, user):
        if self.borrowed_by == user or self.reserved_by == user:

            if self.borrowed_by:
                for i in range(len(user.borrowed_books)):
                    if self.isbn == user.borrowed_books[i].isbn:
                        user.borrowed_books.pop(i)
                        break
            else:
                for i in range(len(user.reserved_books)):
                    if self.isbn == user.reserved_books[i].isbn:
                        user.reserved_books.pop(i)
                        break

            self.borrowed_by = None
            self.reserved_by = None
            logging.info(f'{self.name} has been returned by {user.name}')
            return True
        return False

    def reserve_book(self, user):
        if self.reserved_by or self.borrowed_by:
            logging.debug(f'{self.name} is already reserved or borrowed')
            return False

        self.reserved_by = user
        user.reserved_books.append(self)
        return True

    def edit_book(self, user, **kwargs):
        if not user.is_librarian():
            logging.info(f'{user.name} cannot edit books!')
            return False

        if 'name' in kwargs:
            self.name = kwargs.get('name')

        if 'author' in kwargs:
            self.author = kwargs.get('author')

        if 'isbn' in kwargs:
            self.isbn = kwargs.get('isbn')

        return True

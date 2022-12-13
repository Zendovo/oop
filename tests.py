import unittest
import os
from openpyxl import Workbook
from Book import Book
from Shelf import Shelf
from User import Librarian, User

class TestLibrary(unittest.TestCase):

    def test_book_user(self):
        user1 = User('John')
        user2 = User('Joe')

        book1 = Book('1984', 'George Orwell', 1234567890)
        book2 = Book('Fahrenheit 451', 'Ray Bradbury', 1234567891)

        self.assertEqual(book1.reserve_book(user1), True, 'Reserve book')
        self.assertEqual(book1.reserved_by, user1)
        self.assertEqual(book1.borrowed_by, None)

        self.assertEqual(book1.reserve_book(user2), False, 'Reserve already reserved book')
        self.assertEqual(book1.borrow_book(user2), False, 'Borrow already reserved book')

        self.assertEqual(book1.borrow_book(user1), True, 'Borrow reserved book')
        self.assertEqual(book1.borrowed_by, user1)
        self.assertEqual(book1.reserved_by, None)

        self.assertEqual(book2.borrow_book(user2), True, 'Borrow book')
        self.assertEqual(book2.borrowed_by, user2)
        self.assertEqual(book2.reserved_by, None)

        self.assertEqual(book2.reserve_book(user1), False, 'Reserve borrowed book by another user')
        self.assertEqual(book2.reserve_book(user2), False, 'Reserve borrowed book by borrowing user')

        self.assertEqual(book2.return_book(user1), False, 'Return book as another user')
        self.assertEqual(book2.return_book(user2), True, 'Return book as correct user')

    def test_book_librarian(self):
        user1 = User('John')
        lib1 = Librarian('Miles')
        book1 = Book('1984', 'George Orwell', 1234567890)

        self.assertEqual(book1.edit_book(user1), False, 'Edit book as user should fail')
        
        book1.edit_book(lib1, isbn=3456789123)
        self.assertEqual(book1.isbn, 3456789123, 'Edit book as librarian')

    def test_shelf(self):
        shelf1 = Shelf()
        user1 = User('John')
        lib1 = Librarian('Miles')
        book1 = Book('1984', 'George Orwell', 1234567890)
        book2 = Book('Fahrenheit 451', 'Ray Bradbury', 1234567891)

        self.assertEqual(shelf1.add_book(user1, book1), False, 'Add book to shelf by user should fail')
        self.assertEqual(shelf1.remove_book(user1, 0), False, 'Add book to shelf by user should fail')
        self.assertEqual(shelf1.add_book(lib1, book1), True, 'Add book to shelf by librarian')

        self.assertListEqual(shelf1.show_catalog(), [book1])

        shelf1.add_book(lib1, book2)
        self.assertListEqual(shelf1.show_catalog(), [book1, book2])

        shelf1.remove_book(lib1, 1)
        self.assertListEqual(shelf1.show_catalog(), [book1])

        self.assertRaises(IndexError, shelf1.remove_book, lib1, 1)
        self.assertEqual(shelf1.get_books_count(), 1)

    def test_populate(self):
        # Create a temporary excel sheet with data
        wb = Workbook()
        ws = wb.active

        rows = (('1984', 1234567890, 'George Orwell'), ('Fahrenheit 451', 1234567891, 'Ray Bradbury'), ('Angels and Demons', 3585668585, 'Dan Brown'))
        ws.append(('Name', 'ISBN', 'Author'))
        
        for row in rows:
            ws.append(row)

        filename = 'unit_test.xlsx'
        wb.save(filename)

        shelf1 = Shelf()
        shelf1.populate_book(filename)

        self.assertEqual(shelf1.get_books_count(), len(rows))
        self.assertEqual(shelf1.show_catalog()[0].name, rows[0][0])

        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
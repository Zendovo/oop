from openpyxl import load_workbook
from User import Librarian
from Book import Book


def populate(shelf, file_name):
    wb = load_workbook(file_name)
    ws = wb.active

    rows = ws.rows
    t_rows = tuple(rows)
    for i in range(1, len(t_rows)):
        row = t_rows[i]
        user = Librarian('Script')
        book = Book(row[0].value, row[2].value, row[1].value)
        shelf.add_book(user, book)
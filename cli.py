from Book import Book
from Shelf import Shelf
from User import User, Librarian
import os


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


current_user = None
shelves = []


def main():
    global current_user
    while (True):

        clear()
        print('--------------------------------------------------------------------')
        print('Library Management System')
        print('--------------------------------------------------------------------')
        print('Please enter your name: ')
        name = input()
        print('Login as librarian (Y or else): ')
        libr = input()

        libr = True if libr.upper() == 'Y' else False

        current_user = Librarian(name) if libr else User(name)
        if not libr:
            user_menu()
        else:
            lib_menu()


def lib_menu():
    clear()
    global current_user
    action = 10

    args = tuple()

    while action != 3:
        if action == 10:
            clear()
            print('--------------------------------------------------------------------')
            print(f'Welcome Librarian {current_user.name}')
            print('--------------------------------------------------------------------')
            print('1. Manage shelves')
            options = [20, 3]
            print('*. Exit')

            print('Choose action: ')
            action = int(input())
            action = min(action, 2)
            action = options[action - 1]

        if action == 20:
            out = manage_shelves(*args)
            action = out[0]
            args = tuple(out[1:])
            continue
        if action == 30:
            out = manage_shelf(*args)
            action = out[0]
            args = tuple(out[1:])
            continue
        if action == 31:
            out = manage_catalog(*args)
            action = out[0]
            args = tuple(out[1:])
            continue
        if action == 32:
            out = add_book(*args)
            action = out[0]
            args = tuple(out[1:])
            continue
        if action == 33:
            out = populate_shelf(*args)
            action = out[0]
            args = tuple(out[1:])
            continue
        if action == 40:
            out = manage_book(*args)
            action = out[0]
            args = tuple(out[1:])
            continue
        if action == 41:
            out = edit_book(*args)
            action = out[0]
            args = tuple(out[1:])
            continue
    return


# l20
def manage_shelves():
    clear()

    print('--------------------------------------------------------------------')
    print('Shelves: ')

    for i in range(len(shelves)):
        print('Shelf', i+1)

    print()
    shelf = -1
    while not (shelf <= len(shelves) and shelf > 0):
        print('Choose shelf: ')
        shelf = int(input())

    return (30, shelf - 1)


# l30
def manage_shelf(shelf_index):
    clear()

    print('--------------------------------------------------------------------')
    print(f'Shelf {shelf_index}')
    print('--------------------------------------------------------------------')
    print()
    print('1. Manage catalog')
    print('2. Add book')
    print('3. Populate shelf')
    print('*. Back')
    print()

    action = int(input('Enter action: '))
    if action == 1:
        return (31, shelf_index)
    elif action == 2:
        return (32, shelf_index)
    elif action == 3:
        return (33, shelf_index)
    else:
        return (20,)


# l31
def manage_catalog(shelf_index):
    clear()

    count = shelves[shelf_index].get_books_count()
    books = shelves[shelf_index].show_catalog()
    print('--------------------------------------------------------------------')
    print(f'{count} books in the shelf')
    print()

    for i in range(len(books)):
        book = books[i]
        print(f'{i+1}. {book.name} - {book.author}')

    book = 0
    while not (book <= len(books) and book > 0):
        print('Choose book: ')
        book = int(input())
        print(book)

    return (40, books[book - 1], shelf_index, book - 1)


# l32
def add_book(shelf_index):
    clear()

    name = input("Enter book title")
    author = input("Enter book author")
    isbn = input("Enter book ISBN")

    book = Book(name, author, isbn)
    shelves[shelf_index].add_book(book)

    return (30, shelf_index)


# l33
def populate_shelf(shelf_index):
    clear()

    sheet = input("Enter sheet name")
    shelves[shelf_index].populate_book(sheet)

    return (30, shelf_index)


# l40
def manage_book(book, shelf_index, book_index):
    clear()

    print('--------------------------------------------------------------------')
    print(f'{book.name} - {book.author}')
    print(f'ISBN: {book.isbn}')
    print()

    print('1. Edit details')
    print('2. Remove book')
    print('*. Back')

    action = int(input('Enter action: '))
    if action == 1:
        return (41, book)
    elif action == 2:
        shelves[shelf_index].remove_book(current_user, book_index)
        return (20,)
    else:
        return (20,)


# l41
def edit_book(book):
    print('Enter new details or leave empty to leave unchanged')
    name = input("Enter name: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")

    book.edit_book(current_user, name=name, author=author, isbn=isbn)
    return (20,)


# 10
def user_menu():
    global current_user
    action = 10

    args = tuple()

    while action != 3:
        if action == 10:
            clear()
            print('--------------------------------------------------------------------')
            print(f'Welcome {current_user.name}')
            print('--------------------------------------------------------------------')
            print('1. See books')
            option = 1
            options = [11]
            if len(current_user.borrowed_books) > 0:
                option += 1
                print(str(option) + '. My borrowed books')
                options.append(12)
            if len(current_user.reserved_books) > 0:
                option += 1
                print(str(option) + '. My reserved books')
                options.append(13)
            print('*. Exit')

            print('Choose action: ')
            action = int(input())
            action = options[action - 1]
        if action == 11:
            out = show_shelves(*args)
            action = out[0]
            args = tuple(out[1:])
            continue
        if action == 12:
            out = show_borrowed(*args)
            action = out[0]
            args = tuple(out[1:])
            continue
        if action == 13:
            out = show_reserved(*args)
            action = out[0]
            args = tuple(out[1:])
            continue

        if action == 20:
            out = show_shelves(*args)
            action = out[0]
            args = tuple(out[1:])
            continue
        if action == 30:
            out = show_borrowed(*args)
            action = out[0]
            args = tuple(out[1:])
            continue
        if action == 40:
            out = show_reserved(*args)
            action = out[0]
            args = tuple(out[1:])
            continue
        if action == 50:
            out = show_books(*args)
            action = out[0]
            args = tuple(out[1:])
            continue
        if action == 60:
            out = book_menu(*args)
            action = out[0]
            args = tuple(out[1:])
            continue
    return


# 20
def show_shelves():
    global current_user
    clear()

    print('--------------------------------------------------------------------')
    print('Shelves: ')

    for i in range(len(shelves)):
        print('Shelf', i+1)

    print()
    shelf = -1
    while not (shelf <= len(shelves) and shelf > 0):
        print('Choose shelf: ')
        shelf = int(input())

    print('test')
    return (50, shelf - 1)


# 30
def show_borrowed():
    clear()
    print('--------------------------------------------------------------------')
    print('Borrowed books: ')
    print()
    books = current_user.borrowed_books
    for i in range(len(books)):
        book = books[i]
        print(f'{i+1}. {book.name} - {book.author}')

    book = 0
    while not (book <= len(books)+1 and book > 0):
        print('Choose book: ')
        book = int(input())
        print(book)

    return (60, books[book - 1])


# 40
def show_reserved():
    clear()
    print('--------------------------------------------------------------------')
    print('Reserved books: ')
    print()
    books = current_user.reserved_books
    for i in range(len(books)):
        book = books[i]
        print(f'{i+1}. {book.name} - {book.author}')

    book = 0
    while not (book <= len(books) and book > 0):
        print('Choose book: ')
        book = int(input())
        print(book)

    return (60, books[book - 1])


# 50
def show_books(shelf_index):
    shelf = shelves[shelf_index]

    count = shelf.get_books_count()
    books = shelf.show_catalog()

    clear()
    print('--------------------------------------------------------------------')
    print(f'{count} books in the shelf')
    print()

    for i in range(len(books)):
        book = books[i]
        print(f'{i+1}. {book.name} - {book.author}')

    book = 0
    while not (book <= len(books) and book > 0):
        print('Choose book: ')
        book = int(input())
        print(book)

    return (60, books[book - 1], shelf_index)


# 60
def book_menu(book, shelf_index=None):
    clear()
    print('--------------------------------------------------------------------')
    print(f'{book.name} - {book.author}')
    print(f'ISBN: {book.isbn}')
    print()
    option = 0
    options = []
    if (book.borrowed_by == None and book.reserved_by == None) or book.reserved_by == current_user:
        option += 1
        print(str(option) + '. Borrow book')
        options.append(10)
    elif book.reserved_by == current_user or book.borrowed_by == current_user:
        option += 1
        print(str(option) + '. Return book')
        options.append(20)
    if book.reserved_by == None and book.borrowed_by == None:
        option += 1
        print(str(option) + '. Reserve book')
        options.append(30)
    if not shelf_index == None:
        option += 1
        print(str(option) + '. Back')
        options.append(40)
    print('*. Main Menu')
    options.append(50)

    print('Choose an action: ')
    action = int(input())
    action = min(action, 4)
    action = options[action-1]

    if action == 10:
        res = book.borrow_book(current_user)
        if not res:
            clear()
            print('Book already taken')
            print('Press enter to proceed')
            input()
            return (60, book, shelf_index)
        return (10,)
    elif action == 20:
        res = book.return_book(current_user)
        if not res:
            clear()
            print('Book already taken')
            print('Press enter to proceed')
            return (60, book, shelf_index)
        return (10,)
    elif action == 30:
        res = book.reserve_book(current_user)
        if not res:
            clear()
            print('Book already taken')
            print('Press enter to proceed')
            return (60, book, shelf_index)
        return (10,)
    elif action == 40:
        return (20,)
    else:
        return (10,)


if __name__ == '__main__':
    shelf1 = Shelf()
    shelf1.populate_book('data.xlsx')
    shelves.append(shelf1)
    clear()
    main()

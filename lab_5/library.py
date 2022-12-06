from time import localtime
from string import ascii_lowercase
from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, id: int, author: str, title: str):
        self.id = id
        self.author = author
        self.title = title
        self.pesel = None
    
    def __str__(self):
        return f'{self.id:4d}: {self.author.title():>13} - {self.title.title()}'

class Date:
    def __init__(self, day, month, year, hour, minute, second):
        self.day = day
        self.month = month
        self.year = year
        self.hour = hour % 24
        self.minute = minute
        self.second = second
    
    def __str__(self):
        return f'{self.day:02d}.{self.month:02d}.{self.year:04d} {self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    
def parseDate():
    return Date(localtime().tm_mday, localtime().tm_mon, localtime().tm_year, localtime().tm_hour, localtime().tm_min, localtime().tm_sec)


class BorrowedBook(Book):
    def __init__(self, id, author, title):
        super().__init__(id, author, title)
        self.borrow_date = None
        self.return_date = None

    def __str__(self):
        return f'{self.id:4d}: {self.author.title():>13} - {self.title.title()}'


class BoughtBook(Book):
    def __init__(self, id: int, author: str, title: str, price: int):
        super().__init__(id, author, title)
        self.price = price
        self.bought = False

    def __str__(self):
        return f'{self.id:4d}: {self.author.title():>13} - {self.title.title()}'
        

class Library:
    borrowed_books = []
    readers = []
    borrow_history = []
    transactions = []
    income = 0
    
    def __str__(self):
        print('Books:')
        for book in self.borrowed_books:
            print(book)
        print('\nReaders:')
        for reader in self.readers:
            print(reader)
        print('\nBorrow history:')
        print(f'| Name        | Surname       |  Status  |     Author - Title                                              |   id | Date                |')
        print(f'|-------------|---------------|----------|-----------------------------------------------------------------|------|---------------------|')
        for borrow_entry in self.borrow_history:
            print(borrow_entry)
        print('\nTransactions:')
        print(f'| Title      | Author                                             | Price |')
        print(f'|------------|----------------------------------------------------|-------|')
        for transaction in self.transactions:
            print(transaction)
        sold_books = 0
        for book in self.bought_books:
            if book.bought:
                sold_books += 1
        print(f'\nSold books: {sold_books}')

        print(f'\nIncome: {self.income}')
        return ''

    @staticmethod
    def parseFile():
        borrowed_books = []
        bought_books = []
        bought = False
        id = 1
        with open('C:\\Users\\Studia\\Studia\\Programowanie Skryptowe\\lab_5\\books.txt', 'r') as file:
            for line in file:
                book = line.rstrip().split()

                if len(book) == 3:
                    for _ in range(int(book[2])):
                        borrowed_books.append(BorrowedBook(id, book[1], book[0]))
                        id += 1
                elif len(book) == 4:
                     for _ in range(int(book[2])):
                        bought_books.append(BoughtBook(id, book[1], book[0], book[3]))
                        id += 1
        return borrowed_books, bought_books
    borrowed_books, bought_books = parseFile()


class Reader():
    def __init__(self, name: str, surname: str, pesel: int):
        self.name = name
        self.surname = surname
        self.pesel = pesel

    def __str__(self):
        return f'{self.pesel}: {self.name.title()} {self.surname.title()}'

    def __add__(self, book: BorrowedBook):
        # check title
        ishere = False
        for entry in Library.borrowed_books:
            if entry.title == book.title:
                ishere = True
                break
        if not ishere:
            print('No such title')
            return 'No such title'

        # check author
        ishere = False
        for entry in Library.borrowed_books:
            if entry.author == book.author:
                ishere = True
                break
        if not ishere:
            print('No such author')
            return 'No such author'

        for entry in Library.borrowed_books:
            if entry.title == book.title and entry.author == book.author and entry.pesel == self.pesel:
                print('You have that book already')
                return None
        
        for entry in Library.borrowed_books:
            if entry.title == book.title and entry.author == book.author and not entry.pesel:
                entry.pesel = self.pesel
                entry.borrow_date = parseDate()
                entry.return_date = None
                Library.borrow_history.append(f'| {self.name.title():11} | {self.surname.title():13} | borrowed | {entry.author.title():>10} - {entry.title.title():50} | {entry.id:4d} | {entry.borrow_date} |')
                break

        for reader in Library.readers:
            if self.name == reader.name and self.surname == reader.surname and self.pesel == reader.pesel:
                return None
        Library.readers.append(self)


    def __sub__(self, book: BorrowedBook):
        for entry in Library.borrowed_books:
            if entry.title == book.title and entry.author == book.author and entry.pesel == self.pesel:
                entry.pesel = None
                entry.borrow_date = None
                entry.return_date = parseDate()
                Library.borrow_history.append(f'| {self.name.title():11} | {self.surname.title():13} | returned | {entry.author.title():>10} - {entry.title.title():50} | {entry.id:4d} | {entry.return_date} |')
                return "Retruned"
        print("You don't have that book")
        return "You don't have that book"

    def __lt__(self, book: BoughtBook):
        # check title
        ishere = False
        for entry in Library.bought_books:
            if entry.title == book.title:
                ishere = True
                break
        if not ishere:
            print('No such title')
            return 'No such title'

        # check author
        ishere = False
        for entry in Library.bought_books:
            if entry.author == book.author:
                ishere = True
                break
        if not ishere:
            print('No such author')
            return 'No such author'

        for entry in Library.bought_books:
            if entry.title == book.title and entry.author == book.author and entry.pesel == self.pesel:
                print('You have that book already')
                return None
        
        for entry in Library.bought_books:
            if entry.title == book.title and entry.author == book.author and not entry.bought:
                entry.pesel = self.pesel
                Library.transactions.append(f'| {entry.author.title():>10} - {entry.title.title():50} | {entry.price.title():5} |')
                Library.income += int(entry.price)
                entry.bought = True
                break

        for reader in Library.readers:
            if self.name == reader.name and self.surname == reader.surname and self.pesel == reader.pesel:
                return None
        Library.readers.append(self)


def parseInput(input):
    # Fiu Bzdziu + ostatnie_zyczenie sapkowski

    entry = input.split()
    name, surname, pesel, operation, title, author = entry
    for letter in name.lower():
        if letter not in ascii_lowercase:
            return "Wrong name"
    for letter in surname.lower():
        if letter not in ascii_lowercase:
            return "Wrong surname"
    for digit in pesel:
        if not digit.isdigit():
            return "Wrong pesel"
    if operation not in '+-':
        return "Wrong operation"

    if operation == '+':
        Reader(name, surname, pesel) + Book(0, author, title) 
    elif operation == '-':
        Reader(name, surname, pesel) - Book(0, author, title) 


if __name__ == '__main__':
    date = Date(4, 4, 2032, 24, 12, 0)
    print(date)
    reader = Reader('marcel', 'Trz', 221661247)
    print(reader)
    book1 = BorrowedBook(4, 'sapkowski', 'ostatnie_zyczeni')
    book2 = BorrowedBook(2, 'erikson', 'ogrody_ksiezyca')
    book3 = BoughtBook(0, 'herbert', 'diuna', 30)
    reader + book1
    reader + book2
    reader + book2
    reader - book1
    reader + BorrowedBook(0, 'erikson', 'opowiesci_malazanskiej_ksiegi_poleglych_tom_1')
    reader < book3
    reader < book3
    print(Library.borrowed_books)
    print(Library.bought_books)
    print(Library.transactions)
    print(Library())

    # try:
    #     while True:
    #         parseInput(input('>>> '))
    # except(EOFError):
    #     print(Library())
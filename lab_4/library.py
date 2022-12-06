from time import localtime
from string import ascii_lowercase

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


class Book:
    def __init__(self, id: int, author: str, title: str):
        self.id = id
        self.author = author
        self.title = title
        self.borrow_date = None
        self.return_date = None
        self.pesel = None

    def __str__(self):
        return f'{self.id:4d}: {self.author.title():>13} - {self.title.title()}'


class Library:
    books = []
    readers = []
    borrow_history = []
    transactions = []
    
    def __str__(self):
        print('Books:')
        for book in self.books:
            print(book)
        print('\nReaders:')
        for reader in self.readers:
            print(reader)
        print('\nBorrow History:')
        print(f'| Name        | Surname       |  Status  |     Author - Title                                              |   id | Date                |')
        print(f'|-------------|---------------|----------|-----------------------------------------------------------------|------|---------------------|')
        for borrow_entry in self.borrow_history:
            print(borrow_entry)
        print('\nTransactions')
        return ''

    @staticmethod
    def parseFile():
        books = []
        id = 1
        with open('C:\\Users\\Studia\\Studia\\Programowanie Skryptowe\\lab_4\\books.txt', 'r') as file:
            for line in file:
                book = line.split()
                for _ in range(int(book[2])):
                    books.append(Book(id, book[1], book[0]))
                    id += 1
        return books
    books = parseFile()


class Reader():
    def __init__(self, name: str, surname: str, pesel: int):
        self.name = name
        self.surname = surname
        self.pesel = pesel

    def __str__(self):
        return f'{self.pesel}: {self.name.title()} {self.surname.title()}'

    def __add__(self, book: Book):
        # check title
        ishere = False
        for entry in Library.books:
            if entry.title == book.title:
                ishere = True
                break
        if not ishere:
            print('No such title')
            return 'No such title'

        # check author
        ishere = False
        for entry in Library.books:
            if entry.author == book.author:
                ishere = True
                break
        if not ishere:
            print('No such author')
            return 'No such author'


        for entry in Library.books:
            if entry.title == book.title and entry.author == book.author and entry.pesel == self.pesel:
                print('You have that book already')
                return None
        
        for entry in Library.books:
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

    def __sub__(self, book: Book):
        for entry in Library.books:
            if entry.title == book.title and entry.author == book.author and entry.pesel == self.pesel:
                entry.pesel = None
                entry.borrow_date = None
                entry.return_date = parseDate()
                Library.borrow_history.append(f'| {self.name.title():11} | {self.surname.title():13} | returned | {entry.author.title():>10} - {entry.title.title():50} | {entry.id:4d} | {entry.return_date} |')
                return "Retruned"
        print("You don't have that book")
        return "You don't have that book"

    def __lt__(self):
        pass

    def __gt__(self):
        pass


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
    # date = Date(4, 4, 2032, 24, 12, 0)
    # print(date)
    # reader = Reader('marcel', 'Trz', 221661247)
    # print(reader)
    # book1 = Book(4, 'sapkowski', 'ostatnie_zyczeni')
    # book2 = Book(2, 'erikson', 'ogrody_ksiezyca')
    # reader + book1
    # reader + book2
    # reader + book2
    # reader - book1
    # reader + Book(0, 'erikson', 'opowiesci_malazanskiej_ksiegi_poleglych_tom_1')
    # print(Library())

    try:
        while True:
            parseInput(input('>>> '))
    except(EOFError):
        print(Library())
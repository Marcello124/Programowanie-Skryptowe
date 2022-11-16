class Library:

    def __init__(self):
        self.books = Library.parseFileLine('C:\\Users\\Studia\\Studia\\Programowanie Skryptowe\\lab_4\\config.txt')
        self.transactions = {}

    def __str__(self):
        pass

    def book_borrow(self, name, book, quantity):
        if book not in self.books.keys():
            return 'No such book'

        if name == '':
            return 'No name specified'
            
        if quantity <= 0 or not isinstance(quantity, int):
            return 'Invalid quantity'

        for letter in name:
            if letter.isdigit():
                return 'Invalid name'

        if name not in self.transactions.keys() and self.books[book] >= quantity:
            self.transactions.update({name: {book: quantity}})
        elif book not in self.transactions[name].keys:
            self.transactions.update({name: {book: quantity}})
        else: 
            self.transactions[name][book] += quantity
            self.books[book] -= quantity
    

    def book_return(self, name, book, quantity):
        if name not in self.transactions[name].keys:
            return ''
        if book not in self.transactions[name][book].keys:
            return ''
        self.transactions[name][book] -= quantity
        self.books[book] += quantity

    @staticmethod
    def parseFileLine(line):
        with open(line, 'r') as file:
            return {i.split()[0]: int(i.split()[1]) for i in file.readlines()}

    @staticmethod
    def parseInputLine(line):
        pass


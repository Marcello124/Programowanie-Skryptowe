import unittest
from library import Book, Reader, parseInput


class Test_parseInput(unittest.TestCase):
    
    def test_wrong_name(self):
        self.assertEqual(parseInput('Fiu123 Bzdziu 123 + ostatnie_zyczenie sapkowski'), 'Wrong name')

    def test_wrong_surname(self):
        self.assertEqual(parseInput('Fiu Bzdziu123 123 + ostatnie_zyczenie sapkowski'), 'Wrong surname')

    def test_wrong_pesel(self):
        self.assertEqual(parseInput('Fiu Bzdziu asd + ostatnie_zyczenie sapkowski'), 'Wrong pesel')

    def test_wrong_operation(self):
        self.assertEqual(parseInput('Fiu Bzdziu 123 s ostatnie_zyczenie sapkowski'), 'Wrong operation')


class Test_Reader_Add(unittest.TestCase):

    def test_no_author(self):
        self.assertEqual(Reader('Fiu', 'Bzdziu', 123) + Book(0, 'sapkowski', 'ostatnie_zyczeni'), 'No such title')

    def test_no_title(self):
        self.assertEqual(Reader('Fiu', 'Bzdziu', 123) + Book(0, 'sapkowsk', 'ostatnie_zyczenie'), 'No such author')

    def test_no_more_books(self):
        self.assertEqual(Reader('Fiu', 'Bzdziu', 123) + Book(0, 'herbert', 'diuna'), Reader('Fiu', 'Bzdziu', 123) + Book(0, 'herbert', 'diuna'), 'No such author')

    def test_book_borrowed(self):
        self.assertEqual(Reader('Fiu', 'Bzdziu', 123) + Book(0, 'sapkowski', 'ostatnie_zyczenie'), Reader('Fiu', 'Bzdziu', 123) + Book(0, 'sapkowski', 'ostatnie_zyczenie'), 'No such author')


class Test_Reader_Sub(unittest.TestCase):

    def test_no_book_borrowed(self):
        self.assertEqual(Reader('Fiu', 'Bzdziu', 123) - Book(0, 'erkison', 'ogrody_ksiezyca'), "You don't have that book")



if __name__ == "__main__":
    unittest.main()
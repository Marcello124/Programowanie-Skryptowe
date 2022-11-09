import unittest
from library import Library

class Test_Borrow(unittest.TestCase):

    def test_ok(self):
        self.assertIsNone(Library().book_borrow('Marcin', 'Diuna', 1))

    def test_invalid_name(self):
        self.assertEqual(Library().book_borrow('Marcin123', 'Diuna', 1), "Invalid name")

    def test_no_name(self):
        self.assertEqual(Library().book_borrow('', 'Diuna', 1), "No name specified")

    def test_wrong_book(self):
        self.assertEqual(Library().book_borrow('Marcin', 'kicuch', 1), 'No such book')

    def test_invalid_quantity(self):
        self.assertEqual(Library().book_borrow('Marcin', 'Diuna', -1), 'Invalid quantity')
        self.assertEqual(Library().book_borrow('Marcin', 'Diuna', 2.0), 'Invalid quantity')
        self.assertEqual(Library().book_borrow('Marcin', 'Diuna', 1.2), 'Invalid quantity')


class Test_Return(unittest.TestCase):


    def test_ok(self):
        self.assertIsNone(Library().book_borrow('Marcin', 'Diuna', 1))

    def test_invalid_name(self):
        self.assertEqual(Library().book_borrow('Marcin123', 'Diuna', 1), "Invalid name")

    def test_no_name(self):
        self.assertEqual(Library().book_borrow('', 'Diuna', 1), "No name specified")
        
    def test_wrong_book(self):
        self.assertEqual(Library().book_borrow('Marcin', 'kicuch', 1), 'No such book')

    # def test_too_much(self):
    #     self.assertEqual(Library().book_borrow('Marcin', 'Diuna', 10000000), 'Too many books')

    def test_invalid_quantity(self):
        self.assertEqual(Library().book_borrow('Marcin', 'Diuna', -1), 'Invalid quantity')
        self.assertEqual(Library().book_borrow('Marcin', 'Diuna', 2.0), 'Invalid quantity')
        self.assertEqual(Library().book_borrow('Marcin', 'Diuna', 1.2), 'Invalid quantity')


if __name__ == '__main__':
    unittest.main()
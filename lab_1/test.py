from fractions import Fraction
from typing import Type
import main
import unittest


class Test_TestSum(unittest.TestCase):
    
    def test_sum_integer_integer(self):
        self.assertEqual(main.sum(2, 2), 4)

    def test_sum_integer_float(self):
        self.assertEqual(main.sum(2, 1.5), 3.5)

    def test_sum_integer_string(self):
       self.assertEqual(main.sum(2, '2'), 4)

    def test_sum_string_string(self):
        self.assertEqual(main.sum('2.1', '2.0'), 4.1)

    def test_sum_integer_wrong_number_in_string(self):
        with self.assertRaises(ValueError):
            main.sum(2, 'Ala ma kota123')

    def test_sum_complex_complex(self):
        self.assertEqual(main.sum(complex(2, 2), complex(2, 2)), complex(4, 4))

    def test_sum_complex_int(self):
        self.assertEqual(main.sum(complex(1, 4), 1), complex(2, 4))

    def test_sum_fraction_fraction(self):
        self.assertEqual(main.sum(Fraction(1.5), Fraction(2.4)), Fraction(3.9))

    def test_sum_fraction_int(self):
        self.assertEqual(main.sum(Fraction(1.5), 2), Fraction(3.5))

    def test_sum_nan(self):
        with self.assertRaises(TypeError):
            main.sum(1, [1,])

    def test_str_complex(self):
        self.assertEqual(main.sum('1+1j', 2), 3 + 1j)

if __name__ == '__main__':
    unittest.main()
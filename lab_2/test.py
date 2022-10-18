import main
import unittest

class Test_TestSelling(unittest.TestCase):

    def test_sell_ok(self):
        self.assertEqual(main.sell('apple', 2, 900, 'john'), 'transaction_successful')

    def test_sell_too_much(self):
        self.assertEqual(main.sell('apple', 1000, 900, 'john'), 'out of stock')

    def test_quantity_nan(self):
        self.assertEqual(main.sell('apple', 'sdsasd', 900, 'john'), 'quantity not a number')

    def test_sell_product_dne(self):
        self.assertEqual(main.sell('mouse', 2, 900, 'john'), 'product does not exist')

    def test_sell_surname_not_a_string(self):
        self.assertEqual(main.sell('apple', 2, 900, 'john123'), 'incorrect surname')

    def test_sell_no_surname(self):
        self.assertEqual(main.sell('apple', 2, 900, ''), 'no surname provided')


class Test_TestRefunding(unittest.TestCase):

    def test_refund_ok(self):
        self.assertEqual(main.refund('apple', 2, 900, 'john'), 'transaction_successful')

    def test_refund_too_expensive(self):
        self.assertEqual(main.refund('phone', 1, 900, 'john'), 'ballance too low')

    def test_refund_product_dne(self):
        self.assertEqual(main.refund('mouse', 2, 900, 'john'), 'product does not exist')

    def test_refund_surname_not_a_string(self):
        self.assertEqual(main.refund('apple', 2, 900, 'john123'), 'incorrect surname')

    def test_refund_no_surname(self):
        self.assertEqual(main.refund('apple', 2, 900, ''), 'no surname provided')

class Test_TestLogging(unittest.TestCase):

    def test_log_ok(self):
        self.assertEqual(main.log(['apple', 2, 'john'], {'apple': 3}, 1000), "john bought 2 'apple'\n'apple': 3\nballance: 1000")

    def test_log_empty(self):
        self.assertEqual(main.log([], {'apple': 3}, 1000), "no transactions\n 'apples': 3\nballance: 1000")


if __name__ == '__main__':
    
    unittest.main()
import unittest
from DeanerySystem import term, day


class Test_TestTerm(unittest.TestCase):
    
    def test_normal(self):
        self.assertEqual(term.Term(day.Day.TUE, 9, 45).__str__(), "Tuesday, 9:45 [90]")

    def test_earlierThan(self):
        self.assertEqual(term.Term(day.Day.TUE, 9, 45).earlierThan(term.Term(day.Day.WED, 10, 15)), True )
        self.assertEqual(term.Term(day.Day.WED, 10, 15).earlierThan(term.Term(day.Day.TUE, 9, 45)), False)
        self.assertEqual(term.Term(day.Day.TUE, 9, 45).earlierThan(term.Term(day.Day.TUE, 9, 45)), False)
        

    def test_laterThan(self):
        self.assertEqual(term.Term(day.Day.TUE, 9, 45).laterThan(term.Term(day.Day.WED, 10, 15)), False)
        self.assertEqual(term.Term(day.Day.WED, 10, 15).laterThan(term.Term(day.Day.TUE, 9, 45)), True)
        self.assertEqual(term.Term(day.Day.TUE, 9, 45).laterThan(term.Term(day.Day.TUE, 9, 45)), False)


    def test_equals(self):
        self.assertEqual(term.Term(day.Day.TUE, 9, 45).equals(term.Term(day.Day.WED, 10, 15)), False)
        self.assertEqual(term.Term(day.Day.WED, 10, 15).equals(term.Term(day.Day.TUE, 9, 45)), False)
        self.assertEqual(term.Term(day.Day.TUE, 9, 45).equals(term.Term(day.Day.TUE, 9, 45)), True)


if __name__ == '__main__':
    unittest.main()
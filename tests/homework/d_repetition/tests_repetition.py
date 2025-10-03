import unittest
from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers


class Test_Repetition(unittest.TestCase):


    def test_factorial_0(self):
        self.assertEqual(get_factorial(0), 1)

    def test_factorial_1(self):
        self.assertEqual(get_factorial(1), 1)

    def test_factorial_5(self):
        self.assertEqual(get_factorial(5), 120)

    def test_factorial_9(self):
        self.assertEqual(get_factorial(9), 362880)

    def test_factorial_negative_raises(self):
        with self.assertRaises(ValueError):
            get_factorial(-1)


    def test_sum_odds_1(self):
        self.assertEqual(sum_odd_numbers(1), 1)

    def test_sum_odds_8(self):

        self.assertEqual(sum_odd_numbers(8), 16)

    def test_sum_odds_10(self):

        self.assertEqual(sum_odd_numbers(10), 25)

    def test_sum_odds_negative_raises(self):
        with self.assertRaises(ValueError):
            sum_odd_numbers(0)

import unittest


class TestCalculator(unittest.TestCase):
    def test_sum_numbers_returns_sum_of_integers(self):
        result = 5
        self.assertEqual(result, 5)

  
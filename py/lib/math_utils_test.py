import unittest
import math_utils as mu

class TestPrime(unittest.TestCase) :
    """ test method of math_utils unit
    """
    def test_comb(self):
        value = mu.comb(5, 3)
        expected = 10
        self.assertEqual(expected, value)

        value = mu.comb(23, 10)
        expected = 1144066
        self.assertEqual(expected, value)

    def test_is_palindrome(self):
        value = mu.is_palindrome_num(12021)
        expected = True
        self.assertEqual(expected, value)

        value = mu.is_palindrome_num(12023)
        expected = False
        self.assertEqual(expected, value)

    def test_get_reverse_num(self):
        value = mu.get_reverse_num(12021)
        expected = 12021
        self.assertEqual(expected, value)

        value = mu.get_reverse_num(12023)
        expected = 32021
        self.assertEqual(expected, value)

        value = mu.get_reverse_num(12023)
        expected = 12021
        self.assertNotEqual(expected, value)

    def test_is_pentagonal_num(self):
        value = mu.is_pentagonal_num(12)
        expected = True
        self.assertEqual(expected, value)

        value = mu.is_pentagonal_num(23)
        expected = False
        self.assertEqual(expected, value)

        value = mu.is_pentagonal_num(10000000)
        expected = False
        self.assertEqual(expected, value)

if __name__ == "__main__" :
    unittest.main()

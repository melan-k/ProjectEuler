import unittest
import math_utils as mu

class TestPrime(unittest.TestCase) :
    """ test method of math_utils unit
    """
    def test_comb_small(self):
        value = mu.comb(5, 3)
        expected = 10
        self.assertEqual(expected, value)

    def test_comb_big(self):
        value = mu.comb(23, 10)
        expected = 1144066
        self.assertEqual(expected, value)

if __name__ == "__main__" :
    unittest.main()

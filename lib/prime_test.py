import unittest
import prime

class TestPrime(unittest.TestCase) :
    """ test method of prime unit
    """
    def test_primes_count(self) :
        value = len(prime.each_primes(120))
        expected = 30
        self.assertEqual(expected, value)

if __name__ == "__main__" :
    unittest.main()

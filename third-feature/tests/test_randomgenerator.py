import unittest
from ..RandomGenerator import generateRandomNumber

class TestGenerateRandomNumber(unittest.TestCase):
    def test_generate_random_number(self):
        for _ in range(100):
            result = generateRandomNumber(1, 10)
            self.assertTrue(1 <= result <= 10)

    def test_generate_random_number_no_args(self):
        for _ in range(100):
            result = generateRandomNumber()
            self.assertTrue(0 <= result <= 100)

if __name__ == '__main__':
    unittest.main()
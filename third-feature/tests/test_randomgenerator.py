import unittest
from ..RandomGenerator import generateRandomNumber, generateRandomString

class TestGenerateRandomNumber(unittest.TestCase):
    def test_generate_random_number(self):
        for _ in range(100):
            result = generateRandomNumber(1, 10)
            self.assertTrue(1 <= result <= 10)

    def test_generate_random_number_no_args(self):
        for _ in range(100):
            result = generateRandomNumber()
            self.assertTrue(0 <= result <= 100)

    def test_generate_random_string_default_length(self):
        result = generateRandomString()
        self.assertEqual(len(result), 10)

    def test_generate_random_string_custom_length(self):
        result = generateRandomString(20)
        self.assertEqual(len(result), 20)

    def test_generate_random_string_content(self):
        result = generateRandomString(1000)
        self.assertTrue(all(c in 'abcdefghijklmnopqrstuvwxyz' for c in result))

if __name__ == '__main__':
    unittest.main()
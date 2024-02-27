import unittest

from FirstNewFeature import (addTwoNumbers, cubeRoot, divideTwoNumbers,
                             multiplyTwoNumbers, powerOfTwo, squareRoot,
                             subtractTwoNumbers)

class TestFirstNewFeature(unittest.TestCase):

    def test_add_positive_numbers(self):
        assert addTwoNumbers(1, 2) == 3, "Should be 3"

    def test_add_negative_numbers(self):
        assert addTwoNumbers(-1, -2) == -3, "Should be -3"

    def test_add_zero(self):
        assert addTwoNumbers(0, 5) == 5, "Should be 5"
        assert addTwoNumbers(5, 0) == 5, "Should be 5"
        assert addTwoNumbers(0, 0) == 0, "Should be 0"

    def test_multiply_positive_numbers(self):
        assert multiplyTwoNumbers(2, 3) == 6, "Should be 6"

    def test_multiply_negative_numbers(self):
        assert multiplyTwoNumbers(-2, -3) == 6, "Should be 6"

    def test_multiply_zero(self):
        assert multiplyTwoNumbers(0, 5) == 0, "Should be 0"
        assert multiplyTwoNumbers(5, 0) == 0, "Should be 0"
        assert multiplyTwoNumbers(0, 0) == 0, "Should be 0"

    def test_subtract_positive_numbers(self):
        assert subtractTwoNumbers(5, 3) == 2, "Should be 2"

    def test_subtract_negative_numbers(self):
        assert subtractTwoNumbers(-5, -3) == -2, "Should be -2"

    def test_subtract_zero(self):
        assert subtractTwoNumbers(0, 5) == -5, "Should be -5"
        assert subtractTwoNumbers(5, 0) == 5, "Should be 5"
        assert subtractTwoNumbers(0, 0) == 0, "Should be 0"

    def test_divide_positive_numbers(self):
        assert divideTwoNumbers(6, 3) == 2, "Should be 2"

    def test_divide_negative_numbers(self):
        assert divideTwoNumbers(-6, -3) == 2, "Should be 2"

    def test_divide_zero(self):
        try:
            divideTwoNumbers(5, 0)
        except ZeroDivisionError:
            pass
        else:
            assert False, "Should have raised a ZeroDivisionError"

    def test_power_of_two_positive_number(self):
        assert powerOfTwo(3) == 9, "Should be 9"

    def test_power_of_two_negative_number(self):
        assert powerOfTwo(-3) == 9, "Should be 9"

    def test_power_of_two_zero(self):
        assert powerOfTwo(0) == 0, "Should be 0"

    def test_power_of_two_positive_number(self):
        assert powerOfTwo(3) == 9, "Should be 9"

    def test_power_of_two_negative_number(self):
        assert powerOfTwo(-3) == 9, "Should be 9"

    def test_power_of_two_zero(self):
        assert powerOfTwo(0) == 0, "Should be 0"

    def test_cube_root_positive_number(self):
        assert abs(cubeRoot(8) - 2) < 0.00001, "Should be approximately 2"

    def test_cube_root_zero(self):
        assert cubeRoot(0) == 0, "Should be 0"



if __name__ == '__main__':
    unittest.main()
import unittest

from MoreMaths import calculate_mean, calculate_median, calculate_mode


class TestMoreMaths(unittest.TestCase):

    def test_calculate_mean_positive_numbers(self):
        assert calculate_mean([1, 2, 3, 4, 5]) == 3, "Should be 3"

    def test_calculate_mean_zero(self):
        assert calculate_mean([0, 0, 0, 0, 0]) == 0, "Should be 0"

    def test_calculate_mean_mixed_numbers(self):
        assert calculate_mean([-1, 0, 1]) == 0, "Should be 0"

    def test_calculate_mean_empty_list(self):
        try:
            calculate_mean([])
        except ZeroDivisionError:
            pass
        else:
            assert False, "Should have raised a ZeroDivisionError"

    def test_calculate_median_odd_length(self):
        assert calculate_median([1, 2, 3, 4, 5]) == 3, "Should be 3"

    def test_calculate_median_even_length(self):
        assert calculate_median([1, 2, 3, 4]) == 2.5, "Should be 2.5"

    def test_calculate_median_single_element(self):
        assert calculate_median([1]) == 1, "Should be 1"

    def test_calculate_median_empty_list(self):
        try:
            calculate_median([])
        except IndexError:
            pass
        else:
            assert False, "Should have raised an IndexError"

    def test_calculate_mode(self):
        assert calculate_mode([1, 2, 2, 3, 4]) == 2, "Should be 2"

    def test_calculate_mode_no_repeats(self):
        assert calculate_mode([1, 2, 3, 4, 5]) == 1, "Should be 1"

    def test_calculate_mode_multiple_modes(self):
        assert calculate_mode([1, 1, 2, 2]) in [1, 2], "Should be 1 or 2"

    def test_calculate_mode_empty_list(self):
        try:
            calculate_mode([])
        except ValueError:
            pass
        else:
            assert False, "Should have raised a ValueError"

if __name__ == '__main__':
    unittest.main()
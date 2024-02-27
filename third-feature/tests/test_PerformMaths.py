import unittest

from ..PerformMaths import performCoolMathsTrick


class TestPerformCoolMathsTrick(unittest.TestCase):
    def test_perform_cool_maths_trick(self):
        result = performCoolMathsTrick(1, 2, 3, 4, 5, 9, 8)
        self.assertAlmostEqual(result, 6.1428571428571, places=3)

if __name__ == '__main__':
    unittest.main()
import unittest

from solution import Solution


class TestHeightChecker(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.heightChecker([1, 1, 4, 2, 1, 3]), 3)

    def test_example2(self):
        self.assertEqual(self.solution.heightChecker([5, 1, 2, 3, 4]), 5)

    def test_example3(self):
        self.assertEqual(self.solution.heightChecker([1, 2, 3, 4, 5]), 0)

    def test_additional_case1(self):
        self.assertEqual(self.solution.heightChecker([2, 1, 2, 1, 2]), 4)

    def test_additional_case2(self):
        self.assertEqual(self.solution.heightChecker([10, 6, 8, 5, 9]), 5)


if __name__ == "__main__":
    unittest.main()

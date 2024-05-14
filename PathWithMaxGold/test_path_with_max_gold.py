import unittest

from path_with_max_gold import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
        expected = 24
        self.assertEqual(self.solution.getMaximumGold(grid), expected)

    def test_case2(self):
        grid = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
        expected = 28
        self.assertEqual(self.solution.getMaximumGold(grid), expected)

    def test_case3(self):
        grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = 0
        self.assertEqual(self.solution.getMaximumGold(grid), expected)

    def test_case4(self):
        grid = [[1]]
        expected = 1
        self.assertEqual(self.solution.getMaximumGold(grid), expected)

    def test_case5(self):
        grid = [[0, 1, 0], [0, 0, 0], [0, 1, 0]]
        expected = 1
        self.assertEqual(self.solution.getMaximumGold(grid), expected)


if __name__ == "__main__":
    unittest.main()

import unittest

from safest_path_in_grid import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        grid = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
        self.assertEqual(self.sol.maximumSafenessFactor(grid), 1)

    def test_case_2(self):
        grid = [[0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0]]
        self.assertEqual(self.sol.maximumSafenessFactor(grid), 1)

    def test_case_3(self):
        grid = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
        self.assertEqual(self.sol.maximumSafenessFactor(grid), 1)

    def test_case_4(self):
        grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertEqual(self.sol.maximumSafenessFactor(grid), 1)

    def test_case_5(self):
        grid = [[0, 0], [0, 0]]
        self.assertEqual(self.sol.maximumSafenessFactor(grid), float("inf"))

    def test_case_6(self):
        grid = [[1, 0], [0, 1]]
        self.assertEqual(self.sol.maximumSafenessFactor(grid), 0)

    def test_case_7(self):
        grid = [
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        self.assertEqual(self.sol.maximumSafenessFactor(grid), 1)


if __name__ == "__main__":
    unittest.main()

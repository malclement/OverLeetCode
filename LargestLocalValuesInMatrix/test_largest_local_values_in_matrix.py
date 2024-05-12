import unittest

from largest_local_values_in_matrix import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_largest_local(self):
        grid = [
            [1, 3, 1, 2, 4],
            [2, 1, 3, 1, 4],
            [3, 3, 2, 1, 3],
            [4, 4, 3, 2, 1],
            [2, 2, 1, 3, 4],
        ]
        expected = [[3, 3, 4], [4, 3, 4], [4, 4, 3]]
        self.assertEqual(self.solution.largest_local(grid), expected)

    def test_largest_local_empty(self):
        grid = []
        expected = []
        self.assertEqual(self.solution.largest_local(grid), expected)

    def test_largest_local_single_element(self):
        grid = [[5]]
        expected = []
        self.assertEqual(self.solution.largest_local(grid), expected)

    def test_largest_local_same_elements(self):
        grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected = [[1]]
        self.assertEqual(self.solution.largest_local(grid), expected)


if __name__ == "__main__":
    unittest.main()

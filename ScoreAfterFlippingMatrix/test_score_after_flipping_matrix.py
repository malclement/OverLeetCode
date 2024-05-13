import unittest

from score_after_flipping_matrix import Solution


class TestSolution(unittest.TestCase):
    def test_matrix_score(self):
        solution = Solution()

        # Test case 1
        grid1 = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
        self.assertEqual(solution.matrix_score(grid1), 39)

        # Test case 2
        grid2 = [[0, 1], [0, 1], [0, 1], [1, 1]]
        self.assertEqual(solution.matrix_score(grid2), 14)

        # Test case 3
        grid3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.assertEqual(solution.matrix_score(grid3), 21)


if __name__ == "__main__":
    unittest.main()

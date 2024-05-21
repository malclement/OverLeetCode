import unittest

from subsets import Solution


class TestSubsets(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 2, 3]
        expected_output = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
        result = self.solution.subsets(nums)
        self.assertCountEqual(result, expected_output)

    def test_example2(self):
        nums = [0]
        expected_output = [[], [0]]
        result = self.solution.subsets(nums)
        self.assertCountEqual(result, expected_output)

    def test_empty_input(self):
        nums = []
        expected_output = [[]]
        result = self.solution.subsets(nums)
        self.assertEqual(result, expected_output)

    def test_single_element(self):
        nums = [5]
        expected_output = [[], [5]]
        result = self.solution.subsets(nums)
        self.assertEqual(result, expected_output)

    def test_two_elements(self):
        nums = [1, 2]
        expected_output = [[], [1], [2], [1, 2]]
        result = self.solution.subsets(nums)
        self.assertCountEqual(result, expected_output)

    def test_negative_elements(self):
        nums = [-1, -2, -3]
        expected_output = [
            [],
            [-1],
            [-2],
            [-1, -2],
            [-3],
            [-1, -3],
            [-2, -3],
            [-1, -2, -3],
        ]
        result = self.solution.subsets(nums)
        self.assertCountEqual(result, expected_output)

    def test_mixed_elements(self):
        nums = [-1, 0, 1]
        expected_output = [[], [-1], [0], [-1, 0], [1], [-1, 1], [0, 1], [-1, 0, 1]]
        result = self.solution.subsets(nums)
        self.assertCountEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()

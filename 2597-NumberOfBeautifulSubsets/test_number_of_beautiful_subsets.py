import unittest

from number_of_beautiful_subsets import Solution


class TestBeautifulSubsets(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [2, 4, 6]
        k = 2
        expected_output = 4
        self.assertEqual(self.solution.beautifulSubsets(nums, k), expected_output)

    def test_example2(self):
        nums = [1]
        k = 1
        expected_output = 1
        self.assertEqual(self.solution.beautifulSubsets(nums, k), expected_output)

    def test_large_k(self):
        nums = [1, 3, 5, 7]
        k = 10
        expected_output = 15  # Every subset of [1, 3, 5, 7] is beautiful because k is too large to affect them
        self.assertEqual(self.solution.beautifulSubsets(nums, k), expected_output)

    def test_no_beautiful_subsets(self):
        nums = [1, 2]
        k = 1
        expected_output = 2  # Only single-element subsets [1] and [2] are beautiful
        self.assertEqual(self.solution.beautifulSubsets(nums, k), expected_output)

    def test_all_same_elements(self):
        nums = [5, 5, 5]
        k = 1
        expected_output = (
            7  # All subsets are beautiful because all elements are the same
        )
        self.assertEqual(self.solution.beautifulSubsets(nums, k), expected_output)

    def test_multiple_elements_with_different_k(self):
        nums = [1, 5, 9, 13]
        k = 4
        expected_output = 15  # All subsets are beautiful because all absolute differences are 4 which is valid
        self.assertEqual(self.solution.beautifulSubsets(nums, k), expected_output)

    def test_mixed_elements(self):
        nums = [1, 2, 4, 8]
        k = 3
        expected_output = (
            12  # Various subsets like [1, 4], [1, 2, 8], etc., are beautiful
        )
        self.assertEqual(self.solution.beautifulSubsets(nums, k), expected_output)


if __name__ == "__main__":
    unittest.main()

import unittest

from two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    def test_normal_case(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(two_sum(nums, target), [0, 1])

    def test_no_solution(self):
        nums = [2, 7, 11, 15]
        target = 3
        self.assertIsNone(two_sum(nums, target))

    def test_empty_list(self):
        nums = []
        target = 9
        self.assertIsNone(two_sum(nums, target))

    def test_single_element_list(self):
        nums = [5]
        target = 5
        self.assertIsNone(two_sum(nums, target))

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        self.assertEqual(two_sum(nums, target), [2, 4])

    def test_duplicate_numbers(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(two_sum(nums, target), [0, 1])

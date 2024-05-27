import unittest

from special_array_with_x_element_gte_x import Solution


class TestSpecialArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.specialArray([3, 5]), 2)

    def test_example2(self):
        self.assertEqual(self.solution.specialArray([0, 0]), -1)

    def test_example3(self):
        self.assertEqual(self.solution.specialArray([0, 4, 3, 0, 4]), 3)

    def test_single_element(self):
        self.assertEqual(self.solution.specialArray([1]), 1)
        self.assertEqual(self.solution.specialArray([0]), -1)

    def test_no_special_value(self):
        self.assertEqual(self.solution.specialArray([1, 2, 2, 1]), -1)

    def test_large_numbers(self):
        self.assertEqual(self.solution.specialArray([1000, 1000, 3, 4, 5]), 3)

    def test_multiple_valid_x(self):
        self.assertEqual(self.solution.specialArray([3, 6, 7, 7, 0]), 3)
        self.assertEqual(self.solution.specialArray([1, 2, 2, 6, 6]), 3)


if __name__ == "__main__":
    unittest.main()

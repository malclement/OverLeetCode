import unittest

from single_number import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, 2, 1, 3, 2, 5]
        result = self.solution.singleNumber(nums)
        self.assertCountEqual(result, [3, 5])

    def test_example2(self):
        nums = [-1, 0]
        result = self.solution.singleNumber(nums)
        self.assertCountEqual(result, [-1, 0])

    def test_example3(self):
        nums = [0, 1]
        result = self.solution.singleNumber(nums)
        self.assertCountEqual(result, [0, 1])

    def test_additional1(self):
        nums = [4, 1, 2, 1, 2, 3]
        result = self.solution.singleNumber(nums)
        self.assertCountEqual(result, [4, 3])

    def test_additional2(self):
        nums = [2, 2, 3, 4]
        result = self.solution.singleNumber(nums)
        self.assertCountEqual(result, [3, 4])


if __name__ == "__main__":
    unittest.main()

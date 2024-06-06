import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
        groupSize = 3
        result = self.solution.isNStraightHand(hand, groupSize)
        self.assertTrue(result)

    def test_example2(self):
        hand = [1, 2, 3, 4, 5]
        groupSize = 4
        result = self.solution.isNStraightHand(hand, groupSize)
        self.assertFalse(result)

    def test_single_group(self):
        hand = [1, 2, 3]
        groupSize = 3
        result = self.solution.isNStraightHand(hand, groupSize)
        self.assertTrue(result)

    def test_no_possible_groups(self):
        hand = [1, 2, 4, 5]
        groupSize = 3
        result = self.solution.isNStraightHand(hand, groupSize)
        self.assertFalse(result)

    def test_large_group_size(self):
        hand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        groupSize = 6
        result = self.solution.isNStraightHand(hand, groupSize)
        self.assertTrue(result)

    def test_multiple_possible_groups(self):
        hand = [1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10]
        groupSize = 3
        result = self.solution.isNStraightHand(hand, groupSize)
        self.assertTrue(result)

    def test_duplicate_cards(self):
        hand = [1, 1, 2, 2, 3, 3]
        groupSize = 3
        result = self.solution.isNStraightHand(hand, groupSize)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()

import unittest

from longest_common_prefix import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longestCommonPrefix(self):
        self.assertEqual(
            self.solution.longestCommonPrefix(["flower", "flow", "flight"]), "fl"
        )
        self.assertEqual(
            self.solution.longestCommonPrefix(["dog", "racecar", "car"]), ""
        )
        self.assertEqual(self.solution.longestCommonPrefix([]), "")
        self.assertEqual(self.solution.longestCommonPrefix([""]), "")
        self.assertEqual(
            self.solution.longestCommonPrefix(["prefix", "prefix", "prefix"]), "prefix"
        )
        self.assertEqual(self.solution.longestCommonPrefix(["hello", "hell"]), "hell")


if __name__ == "__main__":
    unittest.main()

import unittest

from longest_sub_str import Solution


class TestSolution(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        solution = Solution()

        # Test cases
        self.assertEqual(solution.lengthOfLongestSubstring(""), 0)  # Empty string
        self.assertEqual(
            solution.lengthOfLongestSubstring("abcabcbb"), 3
        )  # Example case
        self.assertEqual(
            solution.lengthOfLongestSubstring("bbbbb"), 1
        )  # All characters are the same
        self.assertEqual(
            solution.lengthOfLongestSubstring("pwwkew"), 3
        )  # Longest substring is "wke"

        # Add your additional test cases here


if __name__ == "__main__":
    unittest.main()

import unittest

from longest_palindromic_substrings import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "babad"
        result = self.solution.longestPalindrome(s)
        self.assertIn(result, ["bab", "aba"])  # Both "bab" and "aba" are valid answers

    def test_example2(self):
        s = "cbbd"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "bb")

    def test_single_character(self):
        s = "a"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "a")

    def test_two_different_characters(self):
        s = "ac"
        result = self.solution.longestPalindrome(s)
        self.assertIn(result, ["a", "c"])

    def test_palindrome(self):
        s = "racecar"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "racecar")

    def test_empty_string(self):
        s = ""
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "")

    def test_no_palindromes(self):
        s = "abcde"
        result = self.solution.longestPalindrome(s)
        self.assertIn(
            result, ["a", "b", "c", "d", "e"]
        )  # Any single character is valid

    def test_mixed_case(self):
        s = "AbaBa"
        result = self.solution.longestPalindrome(s)
        self.assertEqual(result, "aBa")


if __name__ == "__main__":
    unittest.main()

import unittest

from string_to_integer import Solution


class TestMyAtoi(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_integer(self):
        self.assertEqual(self.solution.myAtoi("42"), 42)

    def test_negative_integer(self):
        self.assertEqual(self.solution.myAtoi("-42"), -42)

    def test_positive_integer_with_whitespace(self):
        self.assertEqual(self.solution.myAtoi("   42"), 42)

    def test_negative_integer_with_whitespace(self):
        self.assertEqual(self.solution.myAtoi("   -42"), -42)

    def test_mixed_characters(self):
        self.assertEqual(self.solution.myAtoi("4193 with words"), 4193)

    def test_leading_alphabets(self):
        self.assertEqual(self.solution.myAtoi("words and 987"), 0)

    def test_overflow(self):
        self.assertEqual(self.solution.myAtoi("91283472332"), 2147483647)

    def test_underflow(self):
        self.assertEqual(self.solution.myAtoi("-91283472332"), -2147483648)

    def test_empty_string(self):
        self.assertEqual(self.solution.myAtoi(""), 0)

    def test_single_character(self):
        self.assertEqual(self.solution.myAtoi("3"), 3)

    def test_zero(self):
        self.assertEqual(self.solution.myAtoi("0"), 0)

    def test_leading_plus(self):
        self.assertEqual(self.solution.myAtoi("+1"), 1)

    def test_leading_zeros(self):
        self.assertEqual(self.solution.myAtoi("00000-42a1234"), 0)

    def test_whitespace_only(self):
        self.assertEqual(self.solution.myAtoi("    "), 0)


if __name__ == "__main__":
    unittest.main()

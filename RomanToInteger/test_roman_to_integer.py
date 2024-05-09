import unittest

from roman_to_integer import Solution


class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_romanToInt(self):
        self.assertEqual(self.solution.romanToInt("III"), 3)
        self.assertEqual(self.solution.romanToInt("IV"), 4)
        self.assertEqual(self.solution.romanToInt("IX"), 9)
        self.assertEqual(self.solution.romanToInt("LVIII"), 58)
        self.assertEqual(self.solution.romanToInt("MCMXCIV"), 1994)
        self.assertEqual(self.solution.romanToInt("MMXXIV"), 2024)


if __name__ == "__main__":
    unittest.main()

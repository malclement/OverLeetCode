import unittest

from valid_parentheses import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_string(self):
        self.assertTrue(self.solution.isValid("()"))
        self.assertTrue(self.solution.isValid("()[]{}"))
        self.assertTrue(self.solution.isValid("{[]}"))

    def test_invalid_string(self):
        self.assertFalse(self.solution.isValid("(]"))
        self.assertFalse(self.solution.isValid("([)]"))
        self.assertFalse(self.solution.isValid("{{{{{{"))

    def test_empty_string(self):
        self.assertTrue(self.solution.isValid(""))

    def test_other_characters(self):
        self.assertTrue(self.solution.isValid("(a)"))
        self.assertTrue(self.solution.isValid("a(b)c{d}"))


if __name__ == "__main__":
    unittest.main()

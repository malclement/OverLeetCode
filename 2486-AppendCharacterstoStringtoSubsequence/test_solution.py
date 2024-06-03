import unittest

from solution import Solution


class TestAppendCharacters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "coaching"
        t = "coding"
        self.assertEqual(self.solution.appendCharacters(s, t), 4)

    def test_example2(self):
        s = "abcde"
        t = "a"
        self.assertEqual(self.solution.appendCharacters(s, t), 0)

    def test_example3(self):
        s = "z"
        t = "abcde"
        self.assertEqual(self.solution.appendCharacters(s, t), 5)

    def test_edge_case1(self):
        s = ""
        t = "abc"
        self.assertEqual(self.solution.appendCharacters(s, t), 3)

    def test_edge_case2(self):
        s = "abcdef"
        t = ""
        self.assertEqual(self.solution.appendCharacters(s, t), 0)

    def test_general_case1(self):
        s = "abcde"
        t = "ace"
        self.assertEqual(self.solution.appendCharacters(s, t), 0)

    def test_general_case2(self):
        s = "axbycz"
        t = "abc"
        self.assertEqual(self.solution.appendCharacters(s, t), 0)

    def test_general_case3(self):
        s = "abcdefgh"
        t = "hgfedcba"
        self.assertEqual(self.solution.appendCharacters(s, t), 8)


if __name__ == "__main__":
    unittest.main()

import unittest

from palindrome_partitioning import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        s = "aab"
        expected = [["a", "a", "b"], ["aa", "b"]]
        result = self.solution.partition(s)
        self.assertEqual(sorted(result), sorted(expected))

    def test_example2(self):
        s = "a"
        expected = [["a"]]
        result = self.solution.partition(s)
        self.assertEqual(result, expected)

    def test_empty_string(self):
        s = ""
        expected = [[]]
        result = self.solution.partition(s)
        self.assertEqual(result, expected)

    def test_single_character(self):
        s = "b"
        expected = [["b"]]
        result = self.solution.partition(s)
        self.assertEqual(result, expected)

    def test_palindrome_string(self):
        s = "racecar"
        expected = [
            ["r", "a", "c", "e", "c", "a", "r"],
            ["r", "a", "cec", "a", "r"],
            ["r", "aceca", "r"],
            ["racecar"],
        ]
        result = self.solution.partition(s)
        self.assertEqual(sorted(result), sorted(expected))

    def test_non_palindrome_string(self):
        s = "abc"
        expected = [["a", "b", "c"]]
        result = self.solution.partition(s)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

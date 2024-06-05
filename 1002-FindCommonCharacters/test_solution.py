import unittest

from solution import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        words = ["bella", "label", "roller"]
        expected = ["e", "l", "l"]
        result = self.solution.commonChars(words)
        self.assertCountEqual(result, expected)

    def test_example2(self):
        words = ["cool", "lock", "cook"]
        expected = ["c", "o"]
        result = self.solution.commonChars(words)
        self.assertCountEqual(result, expected)

    def test_empty_input(self):
        words = []
        expected = []
        result = self.solution.commonChars(words)
        self.assertEqual(result, expected)

    def test_single_word(self):
        words = ["single"]
        expected = ["s", "i", "n", "g", "l", "e"]
        result = self.solution.commonChars(words)
        self.assertCountEqual(result, expected)

    def test_no_common_characters(self):
        words = ["abc", "def", "ghi"]
        expected = []
        result = self.solution.commonChars(words)
        self.assertEqual(result, expected)

    def test_all_same_words(self):
        words = ["aaa", "aaa", "aaa"]
        expected = ["a", "a", "a"]
        result = self.solution.commonChars(words)
        self.assertCountEqual(result, expected)

    def test_case_sensitive(self):
        words = ["aA", "Aa", "aA"]
        expected = ["a"]
        result = self.solution.commonChars(words)
        self.assertCountEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

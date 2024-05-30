import unittest

from zigzag_conversion import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_convert_example1(self):
        s = "PAYPALISHIRING"
        numRows = 3
        expected = "PAHNAPLSIIGYIR"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)

    def test_convert_example2(self):
        s = "PAYPALISHIRING"
        numRows = 4
        expected = "PINALSIGYAHRPI"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)

    def test_convert_example3(self):
        s = "A"
        numRows = 1
        expected = "A"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)

    def test_convert_single_row(self):
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numRows = 1
        expected = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)

    def test_convert_equal_rows_and_length(self):
        s = "ABCD"
        numRows = 4
        expected = "ABCD"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)

    def test_convert_long_string(self):
        s = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
        numRows = 5
        expected = "TBZXQROHPDJWFYOSUVKGMCOLEATNIRUEOHE"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

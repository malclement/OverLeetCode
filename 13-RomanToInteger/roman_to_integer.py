class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        prev_value = 0

        for i in range(len(s)):
            current_value = roman_values[s[i]]

            if i < len(s) - 1 and roman_values[s[i + 1]] > current_value:
                result -= current_value
            else:
                result += current_value

            prev_value = current_value

        return result

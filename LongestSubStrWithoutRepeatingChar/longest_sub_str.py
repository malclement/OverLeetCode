class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_index = [-1] * 128

        max_length = 0
        start_index = 0

        for end_index, char in enumerate(s):
            char_code = ord(char)
            start_index = max(start_index, char_index[char_code] + 1)
            char_index[char_code] = end_index
            max_length = max(max_length, end_index - start_index + 1)

        return max_length

from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        # Initialize the common frequency counter with the first word's frequency counter
        common_freq = Counter(words[0])

        # Intersect with the frequency counters of the remaining words
        for word in words[1:]:
            common_freq &= Counter(word)

        # Expand the elements based on their frequency in common_freq
        result = []
        for char, count in common_freq.items():
            result.extend([char] * count)

        return result

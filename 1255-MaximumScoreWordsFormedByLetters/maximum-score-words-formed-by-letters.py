from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        # Calculate the score for each word
        def calculate_word_score(word):
            return sum(score[ord(ch) - ord("a")] for ch in word)

        # Memoization dictionary
        memo = {}

        # Recursive function with memoization
        def backtrack(index, available_letters):
            # Convert the available_letters Counter to a tuple to use it as a dictionary key
            available_letters_tuple = tuple(sorted(available_letters.items()))
            if (index, available_letters_tuple) in memo:
                return memo[(index, available_letters_tuple)]

            if index == len(words):
                return 0

            # Calculate the score if we don't use the current word
            max_score = backtrack(index + 1, available_letters)

            # Try to use the current word if possible
            word = words[index]
            word_counter = Counter(word)

            # Check if the current word can be formed with the available letters
            if all(
                word_counter[char] <= available_letters[char] for char in word_counter
            ):
                # Use the current word and reduce the letters count
                for char in word_counter:
                    available_letters[char] -= word_counter[char]

                # Calculate the score for the current word
                current_word_score = calculate_word_score(word)

                # Recur for the next words
                max_score = max(
                    max_score,
                    current_word_score + backtrack(index + 1, available_letters),
                )

                # Backtrack: restore the letters count
                for char in word_counter:
                    available_letters[char] += word_counter[char]

            # Memoize the result
            memo[(index, available_letters_tuple)] = max_score
            return max_score

        # Convert letters to a Counter
        available_letters = Counter(letters)

        # Start the recursion
        return backtrack(0, available_letters)

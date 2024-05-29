# Longest Palindromic Substring

This project contains a Python solution to find the longest palindromic substring in a given string, along with unit tests to verify the solution.

## Problem Statement

Given a string `s`, return the longest palindromic substring in `s`.

### Examples

1. **Example 1:**

   - Input: `s = "babad"`
   - Output: `"bab"` (Note: `"aba"` is also a valid answer.)

2. **Example 2:**
   - Input: `s = "cbbd"`
   - Output: `"bb"`

### Constraints

- `1 <= s.length <= 1000`
- `s` consists of only digits and English letters.

## Solution

The solution uses an approach that expands around potential centers of palindromes to find the longest palindromic substring. The time complexity of this solution is O(n^2), where n is the length of the string.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```

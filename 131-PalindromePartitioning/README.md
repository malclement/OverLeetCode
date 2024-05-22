# Palindrome Partitioning

## Description

Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.

### Example 1

**Input**: `s = "aab"`
**Output**: `[["a","a","b"],["aa","b"]]`

### Example 2

**Input**: `s = "a"`
**Output**: `[["a"]]`

### Constraints

- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.

## Solution

The solution to this problem involves using a backtracking approach to find all possible palindrome partitions of the given string `s`. Below is the implementation of the solution in Python.

## Explanation

1. **Helper Function is_palindrome**:

   - This function checks if a given substring sub is a palindrome by comparing it to its reverse.

2. **Backtracking Function backtrack**:

   - The backtrack function explores all possible partitions of the string starting from the index start.

   - If start equals the length of the string s, the current partition (stored in path) is added to the result list.

   - The function iterates through possible end indices, extracts substrings, and checks if they are palindromes.

   - If a substring is a palindrome, it is added to the current path, and the function recursively explores further partitions starting from the end of this substring.

   - After exploring all possibilities for a given start position, the function backtracks by removing the last added substring from the path.

3. **Result List**:

   - The result list collects all valid palindrome partitions found during the backtracking process.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```

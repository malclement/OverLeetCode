# Longest Common Prefix

## Problem Description

Given an array of strings, find the longest common prefix string amongst them. If there is no common prefix, return an empty string ("").

### Examples:

#### Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

#### Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

## Solution Description

The solution is implemented in Python using the provided `Solution` class. It defines a method `longestCommonPrefix` that takes a list of strings `strs` as input and returns the longest common prefix among them.

The solution iterates through the characters of the shortest string in the list and compares each character with the corresponding characters in other strings. If a mismatch is found, it returns the prefix found so far. If all characters match, it returns the shortest string itself as it's the common prefix. If the input list is empty, it returns an empty string.

To optimize the solution in terms of runtime, an alternative approach can be used where characters of all strings are compared simultaneously, stopping as soon as a mismatch is encountered. This approach reduces the number of character comparisons required, resulting in improved performance.

## Running Tests

To run the tests for this solution, ensure you have Python installed. Then, run the following command in your terminal:

```bash
python test_solution.py
```

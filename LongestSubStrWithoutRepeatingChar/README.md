# Longest Substring Without Repeating Characters

## Description

Given a string s, find the length of the longest substring without repeating characters.

## Problem Overview

The problem requires finding the length of the longest substring within a given string where no characters are repeated. For instance, in the string "abcabcbb", the longest substring without repeating characters is "abc", which has a length of 3.

## Solution Summary

To solve this problem efficiently, the solution utilizes the sliding window technique. It maintains two pointers, start_index and end_index, to represent the current substring under consideration. As the end_index moves forward, it checks whether the current character is already present in the substring between start_index and end_index. If it is, the start_index is updated to the position after the last occurrence of the character, ensuring that no repeating characters are present in the substring. The maximum length of such substrings is tracked and returned as the result.

## Implementation

The problem is implemented in Python using a class named Solution. This class contains a method lengthOfLongestSubstring that takes a string s as input and returns an integer representing the length of the longest substring without repeating characters.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```

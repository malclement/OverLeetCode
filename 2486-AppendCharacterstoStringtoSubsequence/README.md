# Append Characters to Form a Subsequence

## Problem Description

You are given two strings s and t consisting of only lowercase English letters. Your task is to return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

## Solution

The solution involves iterating through both strings to determine how much of t is already a subsequence of s. The difference between the length of t and the length of the matched subsequence gives the number of characters to append.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```

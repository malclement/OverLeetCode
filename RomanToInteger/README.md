# Roman to Integer

## Description

Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M.
Given a Roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

## Problem Statement

Given a string representing a Roman numeral, convert it to an integer. Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

## Solution Approach

We can solve this problem by iterating through the given Roman numeral string and accumulating the integer value. We can also take into account the subtraction rule by comparing the current value with the previous one. By looking ahead, we can determine whether the subtraction rule applies.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```

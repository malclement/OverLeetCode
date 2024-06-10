# Height Checker

## Problem Description

A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. The expected ordering is represented by the integer array `expected` where `expected[i]` is the expected height of the ith student in line.

You are given an integer array `heights` representing the current order that the students are standing in. Each `heights[i]` is the height of the ith student in line (0-indexed).

Return the number of indices where `heights[i]` != `expected[i]`.

## Solution

The solution involves comparing the given `heights` list with its sorted version (`expected`) and counting the indices where the values differ.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```

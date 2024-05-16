# Matrix Maximum Local Value Finder

## Description

This project aims to find the maximum local value for each 3x3 submatrix within a given integer matrix. Given an n x n integer matrix grid, the goal is to generate a new matrix maxLocal such that each element maxLocal[i][j] represents the maximum value of the 3x3 submatrix centered around row i + 1 and column j + 1. In simpler terms, the task is to find the largest value in every contiguous 3x3 matrix within the input grid.

## Implementation

The solution to this problem is implemented in Python 3 using a class named Solution. The main function within this class is largestLocal(grid: List[List[int]]) -> List[List[int]], which takes a 2D list of integers (grid) as input and returns a new 2D list (maxLocal) containing the maximum local values for each 3x3 submatrix.

## Optimized Approach

To optimize the runtime of the largestLocal function, the following approach is used:

Iterate through the original matrix grid once.
Calculate the maximum value of each 3x3 submatrix centered around each element.
Construct the resulting maxLocal matrix based on these precomputed maximum values.

## Test Suite

A test suite is provided using the unittest framework to ensure the correctness of the implementation. The test cases cover various scenarios, including:

Normal cases with different input matrices.
Edge cases such as empty matrices, single-element matrices, and matrices with all elements being the same.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```

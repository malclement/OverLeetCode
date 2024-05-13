# Matrix Score

## Problem Description

You are given an m x n binary matrix grid. A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's). Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers. Return the highest possible score after making any number of moves (including zero moves).

## Solution Description

The implemented solution optimizes the calculation of the highest possible score for the given binary matrix. The steps involved in the solution are as follows:

1. Ensure that the leftmost column has the maximum number of 1s. Since toggling a row or column does not affect the leftmost column's score, we can always toggle rows to ensure the leftmost column has more 1s than 0s.

2. After step 1, toggle any columns where the number of 0s is greater than the number of 1s. This ensures that toggling these columns increases the overall score.

The `matrixScore` function iterates through the matrix to perform these optimizations and calculate the highest possible score. The implementation runs in O(m\*n) time complexity, where m is the number of rows and n is the number of columns in the grid.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```

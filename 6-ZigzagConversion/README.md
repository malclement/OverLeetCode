# Zigzag Conversion

This project implements a solution to the "Zigzag Conversion" problem, where a given string is written in a zigzag pattern on a specified number of rows and then read line by line. The project includes both the solution and unit tests to verify the correctness of the implementation.

## Problem Description

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

P A H N

A P L S I I G

Y I R

And then read line by line: "PAHNAPLSIIGYIR".

### Example 1

- **Input:** s = "PAYPALISHIRING", numRows = 3
- **Output:** "PAHNAPLSIIGYIR"

### Example 2

- **Input:** s = "PAYPALISHIRING", numRows = 4
- **Output:** "PINALSIGYAHRPI"

### Example 3

- **Input:** s = "A", numRows = 1
- **Output:** "A"

## Constraints

- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'.
- 1 <= numRows <= 1000

## Solution

The solution is implemented in Python. It handles the conversion by iterating over the characters in the string and placing them in the appropriate rows while toggling the direction when reaching the first or last row.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```

# Bracket Validity Checker

## Description

This project aims to solve the problem of determining whether a given string containing various types of brackets is valid or not. An input string is considered valid if:

- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Every closing bracket has a corresponding open bracket of the same type.

For example:

- Input: "()" -> Output: True
- Input: "()[]{}" -> Output: True
- Input: "(]" -> Output: False

The problem is solved using Python3 and a stack data structure.

## Solution

The solution involves using a stack to keep track of opening brackets as we iterate through the characters of the input string. When encountering an opening bracket, it is pushed onto the stack. When encountering a closing bracket, we check if it matches the top element of the stack (i.e., the most recently opened bracket). If it matches, we pop the opening bracket from the stack. If it doesn't match or if the stack is empty, the string is invalid. At the end, if the stack is empty, it means all brackets were properly matched and closed, so the string is valid; otherwise, it is invalid.

The solution is implemented in the `Solution` class, which provides a method `isValid` that takes a string containing brackets as input and returns True if the string is valid, and False otherwise.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```

# Card Grouping Problem

This project contains a solution to the problem of determining whether a given set of cards can be rearranged into groups of consecutive cards of a specified size. The solution is implemented in Python and includes a set of unit tests to validate its correctness.

## Problem Statement

Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size `groupSize`, and consists of `groupSize` consecutive cards.

Given an integer array `hand` where `hand[i]` is the value written on the ith card and an integer `groupSize`, return `true` if she can rearrange the cards, or `false` otherwise.

## Example

### Example 1:

- **Input:** hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
- **Output:** true
- **Explanation:** Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]

### Example 2:

- **Input:** hand = [1,2,3,4,5], groupSize = 4
- **Output:** false
- **Explanation:** Alice's hand cannot be rearranged into groups of 4.

## Constraints

- 1 <= hand.length <= 10^4
- 0 <= hand[i] <= 10^9
- 1 <= groupSize <= hand.length

## Solution

The solution is implemented in Python within the `Solution` class. The `isNStraightHand` method determines whether the cards can be rearranged as described.

## Files

- `solution.py`: Contains the `Solution` class with the `isNStraightHand` method.
- `test_solution.py`: Contains unit tests for the `isNStraightHand` method using Python's `unittest` framework.

## Running the Tests

To run the tests, make sure you have Python installed. Then, navigate to the project directory and run:

```sh
python -m unittest test_solution.py
```

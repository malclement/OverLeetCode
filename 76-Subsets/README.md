# Subsets Problem Solution

## Description

This project provides a solution to the problem of generating all possible subsets (the power set) of a given list of unique integers. The solution is implemented in Python and includes a comprehensive test suite using the unittest framework.

#### Problem Statement

Given an integer array nums of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets and can be returned in any order.

#### Example 1:

Input: nums = [1, 2, 3]
Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

#### Example 2:

Input: nums = [0]
Output: [[], [0]]
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All elements of nums are unique.

## Solution

The solution is implemented using an iterative approach to generate all subsets. This approach ensures efficiency in both runtime and memory usage.

#### Approach

Initialization: Start with the result list containing just the empty subset [[]].
Iterate Through nums: For each number num in nums, create new subsets by adding num to each subset already present in result.
Use a list comprehension to generate these new subsets (new_subsets).
Extend the result list with these new subsets.
Return Result: After processing all numbers, result contains all possible subsets of nums.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```

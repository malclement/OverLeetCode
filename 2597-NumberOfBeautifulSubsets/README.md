# Beautiful Subsets Project

## Description

This project aims to solve the problem of counting the number of non-empty beautiful subsets of an array nums given a positive integer k. A subset of nums is considered beautiful if it does not contain two integers with an absolute difference equal to k.

## Problem Statement

You are given an array nums of positive integers and a positive integer k. A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

#### Example 1:

Input: nums = [2, 4, 6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].

#### Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
Constraints
1 <= nums.length <= 20
1 <= nums[i], k <= 1000

## Solution

The solution is implemented using a backtracking approach to explore all possible subsets of the array nums while ensuring that each subset is beautiful.

#### Steps:

Define the Backtracking Function: A recursive function is used to generate all subsets.
Check Subset Validity: While generating subsets, check if the current subset is beautiful by ensuring no two elements have an absolute difference equal to k.
Count Beautiful Subsets: If a subset is beautiful, increment the count.

## Running Tests

To run the test file execute the following command:

```bash
python3 test_longest_sub_str.py
```

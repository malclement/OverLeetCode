# Special Array Problem

## Problem Description

You are given an array nums of non-negative integers. The array nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Note that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

## Examples

1. Example 1:

   Input: nums = [3, 5]
   Output: 2
   Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

2. Example 2:

   Input: nums = [0, 0]
   Output: -1
   Explanation: No numbers fit the criteria for x.
   If x = 0, there should be 0 numbers >= x, but there are 2.
   If x = 1, there should be 1 number >= x, but there are 0.
   If x = 2, there should be 2 numbers >= x, but there are 0.
   x cannot be greater since there are only 2 numbers in nums.

3. Example 3:

   Input: nums = [0, 4, 3, 0, 4]
   Output: 3
   Explanation: There are 3 values that are greater than or equal to 3.
   Constraints
   1 <= nums.length <= 100
   0 <= nums[i] <= 1000

## Solution Description

The solution involves checking for the special value x by sorting the array in descending order and iterating through the sorted list to count the numbers greater than or equal to each possible x.

#### Steps:

Sort the Array: First, sort the array in descending order.
Check Conditions for Special x: Iterate through the sorted array, and for each position i, check if the number of elements greater than or equal to i is exactly i. This is done by checking:
If nums[i - 1] (the (i-1)-th element in the sorted array) is greater than or equal to i.
If i is equal to the length of the array or the i-th element in the sorted array is less than i.
Return the Special x: If such an x is found, return it. If no such x exists after the iteration, return -1.

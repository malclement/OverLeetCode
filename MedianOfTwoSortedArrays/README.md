# Median of Two Sorted Arrays

## Problem Description

Given two sorted arrays `nums1` and `nums2` of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

## Implementation

### Python

The solution in Python follows the approach of binary search to partition both arrays into two parts such that the left half contains elements smaller than the right half. Then, it finds the median based on these partitions. The code ensures that the binary search is performed on the smaller array for optimization. This solution is implemented in the `findMedianSortedArrays` method of the `Solution` class.

### C++

The C++ implementation also follows the same binary search approach as the Python solution. It uses vectors for array storage and standard library functions for handling numerical limits and swapping. The code ensures efficient memory management and numerical computations. The solution is implemented in the `findMedianSortedArrays` method of the `Solution` class.

Both implementations provide a time complexity of O(log (m+n)), ensuring efficient computation of the median for large sorted arrays.

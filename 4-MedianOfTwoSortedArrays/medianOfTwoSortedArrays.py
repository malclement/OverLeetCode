from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to simplify the binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        # Binary search for the partition point in nums1
        low, high = 0, m
        while low <= high:
            partition_nums1 = (low + high) // 2
            partition_nums2 = (m + n + 1) // 2 - partition_nums1

            # Calculate the elements on the left and right sides of the partitions
            max_left_nums1 = (
                float("-inf") if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            )
            min_right_nums1 = (
                float("inf") if partition_nums1 == m else nums1[partition_nums1]
            )
            max_left_nums2 = (
                float("-inf") if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            )
            min_right_nums2 = (
                float("inf") if partition_nums2 == n else nums2[partition_nums2]
            )

            # Check if the partitions are correct
            if max_left_nums1 <= min_right_nums2 and max_left_nums2 <= min_right_nums1:
                # If the total number of elements is odd, return the maximum of the left partitions
                if (m + n) % 2 == 1:
                    return max(max_left_nums1, max_left_nums2)
                # If the total number of elements is even, return the average of the maximum of the left and minimum of the right
                else:
                    return (
                        max(max_left_nums1, max_left_nums2)
                        + min(min_right_nums1, min_right_nums2)
                    ) / 2
            elif max_left_nums1 > min_right_nums2:
                # Move partition_nums1 to the left
                high = partition_nums1 - 1
            else:
                # Move partition_nums1 to the right
                low = partition_nums1 + 1
        # If input is invalid
        raise ValueError("Input arrays are not sorted.")

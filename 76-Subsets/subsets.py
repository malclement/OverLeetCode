from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]  # Start with the empty subset
        for num in nums:
            # For each number in nums, add it to all existing subsets in result
            new_subsets = [curr + [num] for curr in result]
            result.extend(new_subsets)
        return result

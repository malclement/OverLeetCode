from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def backtrack(start, current):
            nonlocal count
            if current:
                count += 1
            for i in range(start, len(nums)):
                if not current or all(abs(nums[i] - num) != k for num in current):
                    current.append(nums[i])
                    backtrack(i + 1, current)
                    current.pop()

        nums.sort()  # Sorting helps to make the checking condition faster
        count = 0
        backtrack(0, [])
        return count

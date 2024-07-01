from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0  # Counter for consecutive odd numbers
        for num in arr:
            if num % 2 != 0:  # Check if the number is odd
                count += 1
                if count == 3:  # Check if we have found three consecutive odd numbers
                    return True
            else:
                count = 0  # Reset the counter if the number is not odd
        return False

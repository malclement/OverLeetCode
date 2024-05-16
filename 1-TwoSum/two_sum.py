from typing import List
from typing import Union


def two_sum(nums: List[int], target: int) -> Union[List[int], None]:
    """
    Finds two numbers in the list that sum up to the target.

    Args:
        nums (List[int]): List of integers.
        target (int): Target sum.

    Returns:
        Union[List[int], None]:
            A list containing the indices of the two numbers that sum up to the target.
            If no such pair is found, returns None.
    """
    if not nums or len(nums) < 2:
        return None

    num_set = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_set:
            return [num_set[complement], i]
        num_set[num] = i
    return None

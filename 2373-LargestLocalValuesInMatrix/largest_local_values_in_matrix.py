from typing import List


class Solution:
    def largest_local(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        max_local = [[0] * (n - 2) for _ in range(n - 2)]  # Initialize max_local matrix

        # Iterate through grid to compute maximum value for each 3x3 submatrix
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                max_val = float("-inf")
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        max_val = max(max_val, grid[i + x][j + y])
                max_local[i - 1][j - 1] = max_val

        return max_local

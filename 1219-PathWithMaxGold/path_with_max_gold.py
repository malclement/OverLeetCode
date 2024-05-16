from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x, y, current_gold):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                return current_gold

            # Collect the gold from the current cell
            original_value = grid[x][y]
            current_gold += original_value
            grid[x][y] = 0  # Mark as visited by setting it to 0

            # Explore in all four directions
            max_gold = current_gold
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                max_gold = max(max_gold, dfs(x + dx, y + dy, current_gold))

            # Unmark the current cell
            grid[x][y] = original_value
            return max_gold

        m, n = len(grid), len(grid[0])
        max_gold_collected = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    max_gold_collected = max(max_gold_collected, dfs(i, j, 0))

        return max_gold_collected

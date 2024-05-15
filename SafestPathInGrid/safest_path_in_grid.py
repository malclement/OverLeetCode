import heapq
from collections import deque
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1: Identify all thieves' positions
        thieves = [(r, c) for r in range(n) for c in range(n) if grid[r][c] == 1]

        # Step 2: Calculate the minimum distance to the nearest thief for each cell using BFS
        distances = [[float("inf")] * n for _ in range(n)]
        queue = deque(thieves)

        for r, c in thieves:
            distances[r][c] = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            r, c = queue.popleft()
            current_distance = distances[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and distances[nr][nc] == float("inf"):
                    distances[nr][nc] = current_distance + 1
                    queue.append((nr, nc))

        # Step 3: Use a max-heap to find the maximum safeness factor path
        max_heap = [(-distances[0][0], 0, 0)]
        visited = [[False] * n for _ in range(n)]

        while max_heap:
            safeness, r, c = heapq.heappop(max_heap)
            safeness = -safeness

            if r == n - 1 and c == n - 1:
                return safeness

            if visited[r][c]:
                continue

            visited[r][c] = True

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    heapq.heappush(
                        max_heap, (-min(safeness, distances[nr][nc]), nr, nc)
                    )

        return 0  # This line is technically unreachable

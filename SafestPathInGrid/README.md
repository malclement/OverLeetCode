# Maximum Safeness Factor Path

## Problem Description

You are given a 0-indexed 2D matrix grid of size n x n, where:

grid[r][c] = 1 represents a cell containing a thief.
grid[r][c] = 0 represents an empty cell.
You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum Manhattan distance from any cell in the path to any thief in the grid.

The goal is to return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c) is one of the cells (r, c + 1), (r, c - 1), (r + 1, c), or (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

## Solution Description

To solve this problem, we follow these steps:

Identify the Position of Thieves: First, we identify all the positions of thieves in the grid.
Compute Distance to Thieves: We use a breadth-first search (BFS) to compute the minimum distance from each cell to the nearest thief. This gives us a distance matrix where each cell contains the minimum distance to any thief.
Pathfinding with Maximum Safeness Factor: We use a priority queue (max-heap) to perform a modified Dijkstra's algorithm to find the path from the top-left corner to the bottom-right corner with the maximum minimum safeness factor.

#### Detailed Steps:

BFS for Distance Calculation:
We initialize a queue with all the positions of the thieves and set their distances to 0 in the distance matrix.
For each cell, we explore its neighbors and update their distances if we find a shorter path to a thief.
Modified Dijkstra's Algorithm:
We use a max-heap to prioritize paths with higher safeness factors.
Starting from the top-left corner, we explore all possible paths to the bottom-right corner, always choosing the path that maximizes the minimum safeness factor encountered so far.

#### Complexity:

The BFS to compute the distance matrix runs in O(n^2).
The modified Dijkstra's algorithm also runs in O(n^2 log n), making the solution efficient for large grids.

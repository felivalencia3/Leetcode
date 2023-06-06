# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # find the biggest continuous group of 1s.
        # loop through all cells, if not in visited, run iterative bfs on them. then try doing recursive dfs.
        # keep a counter of the max area of islands, increment locally each time you move to a new island cell.
        # VERSION 1: Iterative BFS
        """
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(init_i, init_j):
            area = 0
            # iterative bfs
            # initial setup
            q = collections.deque()
            q.append((init_i, init_j))
            # loop until queue is empty
            while q:
                # pop node from queue
                i, j = q.popleft()
                # check if island and valid
                if (i, j) not in visited and i in range(rows) and j in range(cols) and grid[i][j] == 1:
                    # visit, and increment area
                    visited.add((i, j))
                    area += 1
                    # add neighboring nodes
                    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        i_di = i + di
                        j_dj = j + dj
                        if (i_di, j_dj) not in visited:
                            q.append((i_di, j_dj))
            return area

        # go through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, bfs(r, c))

        return max_area
        """
        # VERSION 2: Recursive DFS
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        visited = set()

        def dfs(i, j):
            # Recursive DFS
            # Base case:
            if i not in range(rows) or j not in range(cols) or (i, j) in visited or grid[i][j] != 1:
                return 0
            visited.add((i, j))

            area = 0
            for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                area += dfs(i + di, j + dj)

            return area + 1

        # Loop all cells
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        return max_area

# leetcode submit region end(Prohibit modification and deletion)

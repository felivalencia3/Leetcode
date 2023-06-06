# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
 
        def bfs(r, c):
            # BFS is not recursive, its iterative
            # Uses a queue
            q = collections.deque([(r, c)])
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r_dr = row + dr
                    c_dc = col + dc
                    if r_dr in range(rows) and c_dc in range(cols) and grid[r_dr][c_dc] == "1" and (
                            r_dr, c_dc) not in visited:
                        q.append((r_dr, c_dc))
                        visited.add((r_dr, c_dc))

        for r in range(rows):
            for c in range(cols):
                # Traverse and mark visited
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands
# leetcode submit region end(Prohibit modification and deletion)

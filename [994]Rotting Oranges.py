# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        time, fresh = 0, 0
        rows, cols = len(grid), len(grid[0])
        # Iterate grid to do some pre-work - count fresh oranges and add rotting oranges to queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        while q and fresh:
            # For each minute (each state of the while), loop through items in the queue, pop them and add their
            # neighbors to rotted queue.
            for i in range(len(q)):
                r, c = q.popleft() # popleft for queue, pop for stack
                for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    row, col = r + dr, c + dc
                    # check in bounds and fresh, make rotten
                    if row >= 0 and col >= 0 and row != rows and col != cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append([row, col])
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

# leetcode submit region end(Prohibit modification and deletion)

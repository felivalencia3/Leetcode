# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev_height):
            if (r, c) in visited or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prev_height:
                return

            visited.add((r, c))
            # traverse neighbors
            neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nei in neighbors:
                new_r, new_c = nei
                dfs(new_r, new_c, visited, heights[r][c])

        # Call from top and bottom rows
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        return sorted(list(pac.intersection(atl)))
        # leetcode submit region end(Prohibit modification and deletion)

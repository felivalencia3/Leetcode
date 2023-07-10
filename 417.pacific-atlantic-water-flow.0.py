#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights:
            return []

        pac_visited = set()
        atl_visited = set()
        rows, cols = len(heights), len(heights[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def traverse(i: int, j: int, visited: set[tuple[int, int]]):
            if (i, j) in visited:
                return
            visited.add((i, j))
            for di, dj in directions:
                if 0 <= i + di < rows and 0 <= j + dj < cols:
                    if heights[i + di][j + dj] >= heights[i][j]:
                        traverse(i + di, j + dj, visited)

        for row in range(rows):
            # traverse from first and last column of each row
            traverse(row, 0, pac_visited)
            traverse(row, cols - 1, atl_visited)
        for col in range(cols):
            traverse(0, col, pac_visited)
            traverse(rows - 1, col, atl_visited)

        return list(pac_visited & atl_visited)
# @lc code=end

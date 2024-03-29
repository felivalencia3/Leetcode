#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(i: int, j: int) -> None:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "#"
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    dfs(i + di, j + dj)

        if not grid:
            return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
        


# @lc code=end

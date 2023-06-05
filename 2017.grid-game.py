#
# @lc app=leetcode id=2017 lang=python3
#
# [2017] Grid Game
#

# @lc code=start
class Solution(object):
    def gridGame(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        preRow1, preRow2 = grid[0].copy(), grid[1].copy()
        # build prefix
        for i in range(1, n):
            preRow1[i] += preRow1[i-1]
            preRow2[i] += preRow2[i-1]
        
        res = float("inf")
        for i in range(n):
            top = preRow1[-1] - preRow1[i]
            bottom = preRow2[i-1] if i > 0 else 0 
            res = min(res, max(top,bottom))
        return res
# @lc code=end


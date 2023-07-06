#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                # save top left value, then go in reverse
                topLeft = matrix[top][l + i]
                # move bottom left to top left
                matrix[top][l + i] = matrix[bottom - i][l]
                # move bottom right to bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                # move top right to bottom right
                matrix[bottom][r - i] = matrix[top + i][r]
                # move top left into top right (the one we saved before)
                matrix[top + i][r] = topLeft
                
            r -= 1
            l += 1
                
        
# @lc code=end

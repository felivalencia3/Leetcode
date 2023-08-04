#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        top, bottom = 0, m - 1
        mid_row = (bottom - top) // 2
        mid_l, mid_r = matrix[mid_row][0], matrix[mid_row][-1]
        while not (mid_l <= target <= mid_r):
            if target < mid_l:
                bottom = mid_row - 1
            elif target > mid_r:
                top = mid_row + 1
            if top > bottom:
                return False
            mid_row = top + (bottom - top) // 2
            mid_l, mid_r = matrix[mid_row][0], matrix[mid_row][-1]
        # now target is in the row
        # do binary search again to find target
        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if target < matrix[mid_row][mid]:
                right = mid - 1
            elif target > matrix[mid_row][mid]:
                left = mid + 1
            else:
                return True
        return False
# @lc code=end

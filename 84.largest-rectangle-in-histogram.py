#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights = heights + [0]
        stack = [(int(0), heights[0])] # (index, height)
        maxArea = heights[0]
        for i, h in enumerate(heights):
            start = i
            # this runs when we find the first smaller-than-current bar 
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        return maxArea
# @lc code=end
print(Solution().largestRectangleArea([2,1,5,6,2,3]))

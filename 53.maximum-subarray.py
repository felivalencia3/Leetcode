#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        l, r = 0, 0
        maxSum = 0
        sum_elems = []
        while l < len(nums):
            print(sum_elems)
            
            if r < len(nums) - 1 and nums[r + 1] > currMin:
                r += 1
            else:
                sum_elems = nums[l: r + 1]
                maxSum = sum(nums[l: r + 1])
                l += 1
                r = l
        return maxSum
# @lc code=end
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

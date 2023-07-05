#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        # Main difference is that the first and last houses are adjacent.
        # Decision: rob this house + house + 2, or dont rob this house and rob house + 1
        def houseRobberOne(nums: list[int]) -> int:
            prev1, prev2 = 0, 0
            for n in nums:
                curr = max(prev2 + n, prev1)
                prev2 = prev1
                prev1 = curr
            return prev1
        return max(nums[0], houseRobberOne(nums[1:]), houseRobberOne(nums[:-1])) 


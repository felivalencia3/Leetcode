#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if dp[i + j]:
                    dp[i] = True
                    break
        print(dp)
        return dp[0]
# @lc code=end
print(Solution().canJump([3,2,1,0,4]))

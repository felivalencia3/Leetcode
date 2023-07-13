#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * (n + 1)
        max_length = 0
        for i in range(1, n + 1):
            curr = max([dp[i - j] for j in range(1, i) if nums[i - 1] > nums[i - j - 1]], default=0) + 1
            dp[i] = curr
            max_length = max(max_length, curr)
        return max_length

# @lc code=end
print(Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6]))

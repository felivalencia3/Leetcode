#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for x in nums_set:
            if x - 1 not in nums_set:
                y = x + 1
                while y in nums_set:
                    y += 1
                max_len = max(max_len, y - x)
        return max_len
# @lc code=end
print(Solution().longestConsecutive([4, 1, 3, 2]))

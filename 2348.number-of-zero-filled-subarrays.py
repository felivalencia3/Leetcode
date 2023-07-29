#
# @lc app=leetcode id=2348 lang=python3
#
# [2348] Number of Zero-Filled Subarrays
#

# @lc code=start
class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        def zero_series(n: int) -> int:
            return int((float(n) / 2) * (n + 1))
        zeros = 0
        total = 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif zeros > 0:
                total += zero_series(zeros) 
                zeros = 0
        return total + zero_series(zeros)
# @lc code=end
print(Solution().zeroFilledSubarray([0,0,0,2,0,0]))

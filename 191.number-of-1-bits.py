#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= (n - 1)
            ans += 1
        return ans
# @lc code=end
print(Solution().hammingWeight(0b00000000000000000000000000001011))

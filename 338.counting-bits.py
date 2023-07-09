#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for i in range(n + 1):
            curr = i
            count = 0
            while curr:
                count += curr%2
                curr = curr >> 1
            ans[i] = count
        return ans

# @lc code=end

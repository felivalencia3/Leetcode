#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
import time
start = time.time()
class Solution:
    def numDecodings(self, s: str) -> int:
        def decode(curr: int, memo: dict={}) -> int:
            if curr in memo:
                return memo[curr]

            if s == "0" or curr > len(s):
                return 0
            if curr == len(s):
                return 1

            if int(s[curr]) == 0: 
                return 0
            res = decode(curr + 1)
            if int(s[curr: curr + 2]) <= 26:
                res += decode(curr + 2)
            memo[curr] = res
            return res
        return decode(0)

            
# @lc code=end
print(Solution().numDecodings("111111111111111111111111111111111111111111111"))
end = time.time()
print(end - start)


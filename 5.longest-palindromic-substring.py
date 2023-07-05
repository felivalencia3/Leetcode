#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[False] * n for _ in range(n)]
        ans = s[n - 1]
        # make diagonals true
        for i in range(n):
            dp[i][i] = True

        maxLen = 1
        for start in range(n - 1, -1, -1):
            for end in range(start + 1, n):
                if s[start] == s[end]:
                    if end - start == 1 or dp[start + 1][end - 1]:
                        dp[start][end] = True
                        if end - start + 1 > maxLen:
                            maxLen = end - start + 1
                            ans = s[start: end + 1]
        return ans
# Input to test:  "abbcccbbbcaaccbababcbcabca"
# @lc code=end
print(Solution().longestPalindrome("baba"))

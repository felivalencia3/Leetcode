#
# @lc app=leetcode id=1930 lang=python
#
# [1930] Unique Length-3 Palindromic Subsequences
#

# @lc code=start
from collections import Counter, defaultdict
class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = set()
        left = set()
        right = Counter(s)

        for i in range(len(s)):
            right[s[i]] -= 1
            if right[s[i]] == 0:
                right.pop(s[i])
            
            for c in "abcdefghijklmnopqrstuvwxyz":
                if c in left and c in right:
                    res.add((s[i], c))
            left.add(s[i])
            
        return len(res)
# @lc code=end
s = "tlpjzdmtwderpkpmgoyrcxttiheassztncqvnfjeyxxp"
print(Solution().countPalindromicSubsequence(s))
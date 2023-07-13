#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
from typing import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # keep a missing[char] dict 
        # expand window, then contract once need[char] == 0
        # keep a minWindow tuple
        if not s or not t or len(s) < len(t):
            return ""

        need = Counter(t)
        count = sum(need.values())
        minWindow = (0, float("inf"))
        l = 0

        for i in range(len(s)):
            char = s[i]
            if char in need:
                need[char] -= 1
                count -= 1
            if count == 0: # contract
                while l < i and not count:
                    if s[l] in need:
                        need[s[l]] += 1
                        count += 1
                    l += 1
                if i - l + 1 < minWindow[1] - minWindow[0]:
                    minWindow = (l - 1, i)
        return s[minWindow[0]: minWindow[1] + 1] if minWindow[1] <= len(s) else ""
# @lc code=end
print(Solution().minWindow(s = "a", t = "aa"))


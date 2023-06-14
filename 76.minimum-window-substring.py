#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
from collections import Counter, defaultdict


# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialize counters and maps
        res = (float("-inf"), float("inf"))
        have_count = 0
        have = defaultdict(int)
        need = Counter(t)
        need_count = sum(need.values())
        if len(t) > len(s):
            return ""
        # Sliding Window Vars
        l, r = 0, 0
        while r < len(s):
            while have_count < need_count and r < len(s):
                char = s[r]
                if char in need:
                    if have[char] < need[char]:
                        have_count += 1
                    have[char] += 1
                r += 1

            while have_count == need_count:
                removed = s[l]
                if removed in have:
                    have[removed] -= 1
                    if have[removed] < need[removed]:
                        have_count -= 1
                l += 1
            if r - l < res[1] - res[0]:
                res = (l - 1, r)

        return s[res[0] : res[1]]


# @lc code=end
s = "a"
t = "b"
print(Solution().minWindow(s, t))

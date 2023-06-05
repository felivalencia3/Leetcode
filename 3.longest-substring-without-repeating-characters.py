#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_length = 1
        char_idx = {s[0]: 0}
        l, r = 0, 1
        while l <= r and r < len(s):
            if s[r] not in char_idx:
                char_idx[s[r]] = r
                max_length = max(max_length, r - l + 1)
            else:
                if char_idx[s[r]] >= l:
                    l = char_idx[s[r]] + 1 if l != char_idx[s[r]] else l + 1
                    char_idx[s[r]] = r
                else:
                    char_idx[s[r]] = r
                    max_length = max(max_length, r - l + 1)
            r += 1

        return max_length


# @lc code=end
print(Solution().lengthOfLongestSubstring("tmmzuxt"))

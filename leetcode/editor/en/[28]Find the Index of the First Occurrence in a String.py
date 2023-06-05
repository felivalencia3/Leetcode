# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = 0
        # move l forward
        # when h[l] == n[0], start searching with r.
        while l < len(haystack):
            if haystack[l] == needle[0]:
                if haystack[l:l + len(needle)] == needle:
                    return l
            l += 1
        return -1

# leetcode submit region end(Prohibit modification and deletion)

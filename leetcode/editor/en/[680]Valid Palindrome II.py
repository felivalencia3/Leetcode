
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointers,one at start, one at end
        start, end = 0, len(s)-1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                # generate both possible strings, removing start or end.
                remStart = s[0:start] + s[start+1:]
                remEnd = s[0:end] + s[end+1:]
                return remStart == remStart[::-1] or remEnd == remEnd[::-1]
        return True



# leetcode submit region end(Prohibit modification and deletion)
s = "abc"
print(Solution().validPalindrome(s))

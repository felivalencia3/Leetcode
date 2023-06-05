


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codeSet = set()
        for i in range(len(s) - k + 1):
            codeSet.add(s[i: i+k])

        return len(codeSet) == (1 << k)

# leetcode submit region end(Prohibit modification and deletion)

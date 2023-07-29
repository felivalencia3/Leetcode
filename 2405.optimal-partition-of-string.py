#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#

# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:
        if not s:
            return 0
        count = 1
        window = set()
        for char in s:
            if char in window:
                count += 1
                window.clear()
            window.add(char)
        return count
# @lc code=end
print(Solution().partitionString("ssssss"))

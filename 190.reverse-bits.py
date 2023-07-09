#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        # loop all bits of n:
        for i in range(32):
            # shift n to the left by 1, so i-th digit from the right is going to be at end
            # then AND it with 1, this returns whether that i-th digit was 1 or 0
            # then OR the i-th from the left position of res with that number
            # this makes res 1 in that position if bit was 1.
            # Sort of: AND gets a 1, OR gives a 1then OR the i-th from the left position of res with that number
            # this makes res 1 in that position if bit was 1.
            # Sort of: AND gets a 1, OR gives a 1..
            bit = (n >> i) & 1
            res | (bit << (31 - i))
        return res
# @lc code=end
print(Solution().reverseBits(0b00000010100101000001111010011100))

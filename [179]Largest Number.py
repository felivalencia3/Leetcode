# leetcode submit region begin(Prohibit modification and deletion)
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = nums[i]

        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(compare))

        return "".join(map(str, nums))

# leetcode submit region end(Prohibit modification and deletion)


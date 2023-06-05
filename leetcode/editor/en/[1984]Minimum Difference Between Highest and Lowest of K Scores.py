# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        nums.sort()
        l = 0
        currMin = float("inf")
        while l <= len(nums) - k:
            currMin = min(nums[l + k - 1] - nums[l], currMin)
            l += 1

        return currMin



# leetcode submit region end(Prohibit modification and deletion)
nums = [87063,61094,44530,21297,95857,93551,9918]
print(Solution().minimumDifference(nums, 6))


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        def kSum(k, start, helper_target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, helper_target - nums[i])
                    quad.pop()
                return
            left, right = start, len(nums) - 1
           while left < right:
                if nums[left] + nums[right] < helper_target:
                    left += 1
                elif nums[left] + nums[right] > helper_target:
                    right -= 1
                else:
                    res.append(quad + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1

        kSum(4, 0, target)
        return res

# leetcode submit region end(Prohibit modification and deletion)

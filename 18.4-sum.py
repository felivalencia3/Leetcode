#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        # Store all results
        res = []
        quad = []  # Current quadruplet

        # Recursive kSum
        def kSum(k, start, target):
            # we'll substract a, b,c, d... from target
            # non-base case:
            if k != 2:
                # loop from start to end, except for the last k values
                # we need there to be at least k other values for the other remaining values.
                # This loop fixes one value
                for i in range(start, len(nums) - k + 1):
                    # Skip duplicates
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    # Add to current quad
                    quad.append(nums[i])
                    # Run recursive function
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
            else:
                # base case, 2Sum
                l, r = start, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        # Keep incrementing left if there are duplicates (and make sure its still in bounds)
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1

        kSum(4, 0, target)
        return res


# @lc code=end

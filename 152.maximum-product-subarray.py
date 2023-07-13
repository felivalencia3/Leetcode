#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        # loop through the list from the second element
        for num in nums[1:]:
            # if the current number is negative, swap the maximum and minimum products
            if num < 0:
                curr_max, curr_min = curr_min, curr_max
            
            # update the maximum and minimum products with the current number
            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            # update the maximum product with the current maximum product
            max_product = max(max_product, curr_max)
        
        # return the maximum product
        return max_product
# @lc code=end
print(Solution().maxProduct([2,3,-2,4]))

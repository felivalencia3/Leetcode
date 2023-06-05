#
# @lc app=leetcode id=523 lang=python
#
# [523] Continuous Subarray Sum
#

# @lc code=start
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        prefix_sums = {0: -1}
        prefix_sum = 0
        
        # iterate through the array and compute the prefix sums
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if k != 0:
                prefix_sum %= k
                
            # check if there is a previous prefix sum that has the same remainder
            if prefix_sum in prefix_sums:
                # check if the length of the subarray is greater than 1
                if i - prefix_sums[prefix_sum] > 1:
                    return True
            else:
                # store the current prefix sum and its position
                prefix_sums[prefix_sum] = i
        return False
            
        
        
# @lc code=end
nums = [23,2,6,4,7]
k = 13
print(Solution().checkSubarraySum(nums,k))

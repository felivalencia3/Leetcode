#
# @lc app=leetcode id=560 lang=python
#
# [560] Subarray Sum Equals K
#


# @lc code=start
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        # build prefix sum array
        prefix_sum = [0 for _ in nums]
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = nums[i] + prefix_sum[i - 1]

        sum_map = {0: 1}

        for s in prefix_sum:
            if s - k in sum_map:
                count += sum_map[s - k]
            if s in sum_map:
                sum_map[s] += 1
            else:
                sum_map[s] = 1
        return count


# @lc code=end
nums = [1, 2, 1, 2, 1]
# [1,1,1], 2 = 2
# [1,2,3], 3 = 2
# [-1,-1,1,2,-3,1], 0 = 4
k = 3
print(Solution().subarraySum(nums, k))

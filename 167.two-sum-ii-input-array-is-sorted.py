#
# @lc app=leetcode id=167 lang=python
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # start l at 0, r at len(n)
        # if n[l] + n[r] == target, return
        # if n[l] + n[r] < target, l++
        # if n[l] + n[r] > target, r--
        # loop while l < r.
        l, r = 0, len(numbers)-1
        while l < r:
            start = numbers[l]
            end = numbers[r]
            if start + end == target:
                return [l+1,r+1]
            elif start + end < target:
                l += 1
            else:
                r -= 1
        return []
                
        

            
            
                
        
        
# @lc code=end
nums = [2,3,4]
print(Solution().twoSum(nums, 6))

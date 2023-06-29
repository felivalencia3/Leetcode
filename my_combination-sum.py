#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums: List[int], target: int, index: int, path: List[int], res: List[List[int]]):
            if target < 0:
                return
            if target == 0:
                res.append(path)
                return
            for i in range(index, len(nums)):
                dfs(nums, target-nums[i], i, path+[nums[i]], res)
        res = []
        candidates.sort()
        dfs(candidates, target, 0, [], res)
        return res

print(Solution().combinationSum([2,3,6,7], 7))

        
               
# @lc code=end

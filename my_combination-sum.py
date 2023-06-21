#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def findSum(target: int, last: int, memo: dict = {}) -> List[List[int]]:
            if (target, last) in memo:
                return memo[(target, last)]
            if target == 0:
                return [[last]]
            if target < 0:
                return []
            
            curr_res = []
            for num in candidates:
                last_res = findSum(target-num, num, memo)
                if last_res:
                    for pre in last_res:
                        if last:
                            pre.append(last)
                        pre.sort()
                curr_res.extend(last_res)

            memo[(target, last)] = curr_res
            return curr_res
        res = findSum(target, 0)
        return [list(item) for item in set(map(tuple, res))]

print(Solution().combinationSum([2,3,6,7], 7))

        
               
# @lc code=end

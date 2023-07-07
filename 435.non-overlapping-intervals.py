#
# @lc app=leetcode id=435 lang=python3
#
# [435] Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        end = float("-inf")
        count = 0
        for iter in sorted(intervals, key=lambda x: x[1]):
            # if the current start is greater than the last smallest end
            # then there are no more overlapping, we can skip to next intervals
            if iter[0] >= end:
                end = iter[1]
            else: # there is an overlap, just remove iter
                count += 1 
        return count

# @lc code=end
print(Solution().eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))

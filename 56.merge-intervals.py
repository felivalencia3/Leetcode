#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # sort all intervals by start
        intervals = sorted(intervals, key=lambda x:x[0])
        int1, int2 = [], intervals[0]
        res = []
        for i in range(len(intervals) - 1):
            int1, int2 = intervals[i], intervals[i + 1]
            if res and int1[1] >= int2[0]:
                # overlap
                int2[1] = max(int1[1], int2[1])
            else:
                res.append(int1)
        return res
# @lc code=end
print(Solution().merge([[1,4],[0,0]]))

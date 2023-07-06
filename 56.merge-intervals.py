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
        res = []
        int1 = []
        for i in range(len(intervals)):
            int2 = intervals[i]
            if res and res[-1][1] >= int2[0]:
                # overlap
                int1 = res[-1]
                int1[1] = max(int1[1], int2[1])
            else:
                res.append(int2)
        return res
# @lc code=end
print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))

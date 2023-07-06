#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        for interval in intervals: 
            start, end = interval
            # new interval after range of current one, so skip.
            if end < newInterval[0]:
                result.append([start, end])
            # new interval is before current, so add newInterval and continue
            elif newInterval[1] < start:
                result.append(newInterval)
                newInterval = interval 
            else: 
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newIntervaInterval[1])
        result.append(newInterval)
        return result

# @lc code=end
print(Solution().insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))

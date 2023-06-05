#
# @lc app=leetcode id=554 lang=python
#
# [554] Brick Wall
#
from itertools import accumulate


# @lc code=start
class Solution(object):
    @staticmethod
    def leastBricks(wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        countGap = {0: 0}  # map position : count of gaps

        for row in wall:
            total = 0
            for brick in row[:-1]:  # don't count end
                total += brick  # position we're at
                countGap[total] = 1 + countGap.get(total, 0)
                # add 1 to the gap count at that position, add 1 to 0 (default) if does not exist in map yet
        return len(wall) - max(countGap.values())
# @lc code=end

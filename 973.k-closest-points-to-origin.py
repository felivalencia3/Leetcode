#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        distance = lambda point1: sqrt((point1[0] ** 2) + (point1[1] ** 2))
        point_heap = [(distance(point), point) for point in points]
        heapq.heapify(point_heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(point_heap)[1])
        return res

        
# @lc code=end
print(Solution().kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))

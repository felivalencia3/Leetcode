#
# @lc app=leetcode id=1584 lang=python3
#
# [1584] Min Cost to Connect All Points
#

# @lc code=start
import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        # Prim's Algorithm for Minimum Spanning Trees.
        # O(n^2 logn)
        visited = set()
        frontier = [(0, tuple(points[0]))] # (distance, (x, y))
        cost = 0

        while frontier and len(visited) < len(points):
            dist, (x, y) = heapq.heappop(frontier)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            cost += dist

            for (x2, y2) in points:
                if (x2, y2) not in visited:
                    manhattan = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                    heapq.heappush(frontier, (manhattan((x, y), (x2, y2)), (x2, y2)))
        return cost
print(Solution().minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
# @lc code=end

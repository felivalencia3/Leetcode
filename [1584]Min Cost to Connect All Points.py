# leetcode submit region begin(Prohibit modification and deletion)
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        # Create adjacency list (map)
        adj = {i: [] for i in range(N)}  # i: list of [cost, node]

        # Loop all combinations of points, and calculate manhattan distance as edges to add to adj list
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)

                adj[i].append([dist, j])
                adj[j].append([dist, i])

        # Now do Prim's Algorithm
        total_cost = 0
        visit = set()
        minH = [[0, 0]]  # [cost, node]
        while len(visit) < N:
            cost, i = heapq.heappop(minH)
            if i in visit:
                continue
            total_cost += cost
            visit.add(i)
            for neiCost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost, nei])

        return total_cost

# leetcode submit region end(Prohibit modification and deletion)

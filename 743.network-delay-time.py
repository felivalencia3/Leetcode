#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#

# @lc code=start
import heapq

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # 1. build graph representation graph = {src: {neighbor (target): weight}}
        # TODO: Optimize graph representation -> convert to list
        graph = [{} for _ in range(n + 1)]
        visited = set()
        queue = [(0, k)]
        for src, target, weight in times:
            graph[src][target] = weight
        t = 0
        # 2. regular dikstra's, return max dist in distances
        while queue and len(visited) < n:
            dist, node = heapq.heappop(queue)
            visited.add(node)
            t = max(t, dist)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    new_dist = dist + graph[node][neighbor]
                    heapq.heappush(queue, (new_dist, neighbor))
        return t if len(visited) == n else -1
# @lc code=end
res = Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], n = 3, k = 1)
print(res)

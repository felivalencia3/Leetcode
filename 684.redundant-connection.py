#
# @lc app=leetcode id=684 lang=python3
#
# [684] Redundant Connection
#

# @lc code=start
from typing import Optional


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        redundantEdge = []
        parent = [i for i in range(len(edges) + 1)] 
        rank = [1] * (len(edges) + 1)

        def find(n) -> int:
            p = parent[n]
            while p != parent[n]:
                # path compression
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(n1, n2) -> bool:
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False

            if rank[p1] > rank[p2]:
                p1, p2 = p2, p1
            parent[p1] = p2
            rank[p2] += rank[p1]
            return True

        for edge in edges:
            if not union(*edge):
                return [*edge]
# @lc code=end

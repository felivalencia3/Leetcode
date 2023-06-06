# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(u, v, visited, graph):
            # Check if the current node u has already been visited
            if u in visited:
                return False

            # Check if the current node u is the target node v
            if u == v:
                return True

            # Mark the current node u as visited
            visited.add(u)

            # Explore each adjacent node of u
            for i in graph[u]:
                if dfs(i, v, visited, graph):
                    return True

            # If no path is found from u to v, return False
            return False

        def find_path(edges):
            n = len(edges)
            graph = defaultdict(list)
            ans = []

            # Build the graph's adjacency list
            for u, v in edges:
                visited = set()  # Initialize the visited set for each pair of nodes

                # Check if there is a path from u to v
                if dfs(u, v, visited, graph):
                    ans = [u, v]  # Update the answer if a path is found
                # Add the edges to the graph's adjacency list
                graph[u].append(v)
                graph[v].append(u)

            return ans

        return find_path(edges)

# leetcode submit region end(Prohibit modification and deletion)

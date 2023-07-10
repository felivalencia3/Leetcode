#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 1. build graph
        graph = defaultdict(list)
        visited = {}
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # 2. write a DFS function that looks for cycles.
        def dfs(courseNum: int) -> bool:
            if courseNum in visited:
                return not visited[courseNum]

            visited[courseNum] = True
            for nei in graph[courseNum]:
                if not dfs(nei):
                    return False
            visited[courseNum] = False
            return True
        
        # Call from courses with no dependencies
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


        
# @lc code=end
Solution().canFinish(2, [[1, 0]])

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if not preMap[crs]:
                return True

            visited.add(crs)
            # Run DFS for all prerequisite courses
            for pre in preMap[crs]:
                # if any of the courses can't be completed, return False for everything
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)

#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # if already in visited, returning value in visited
        # if in a corner update res tuple (pac, atl) and return
        # else, dfs to neighbors equal or shorter.
        # take their return values, if at least two have pac == 1 and atl == 1, return (1,1) and add (i,j) to res
        # at end of loop return res
        visited = {} # (i,j) : (pac, atl)
        final = set()
        def dfs(i: int, j: int) -> tuple[bool, bool]:
            if (i, j) in visited:
                return visited[(i,j)]

            res = [False, False]
            if (i, j) == (0, len(heights[0]) - 1) or (i,j) == (len(heights) - 1, 0):
                final.add((i, j))
                return (True, True)
            if i == 0 or j == 0:
                # pacific
                res = [True, False]
            if i == len(heights) - 1 or j == len(heights[0]) - 1:
                res = [False, True]

            visited[(i,j)] = res
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i + di < len(heights) and 0 <= j + dj < len(heights[0]) and heights[i + di][j + dj] <= heights[i][j]:
                    pac, atl = dfs(i + di, j + dj)
                    res[0] = True if pac else res[0]
                    res[1] = True if atl else res[1]
                    if res[0] and res[1]:
                        final.add((i, j))
                        visited[(i,j)] = tuple(res)
                        return tuple(res)
            return tuple(res)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) not in visited:
                    dfs(i, j)
        return [list(tup) for tup in final]
# @lc code=end
res = Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
print(res)
print(sorted(res) == sorted([[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]))
# expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

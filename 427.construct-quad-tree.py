#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#

# @lc code=start
# Definition for a QuadTree node.
class Node:
    def __init__(self, val: bool, isLeaf: bool, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: list[list[int]]) -> Node:
        n = len(grid)
        allTrue = True
        someTrue = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                bool_val = bool(grid[i][j])
                allTrue &= bool_val
                someTrue |= bool_val
        if allTrue or not someTrue:
            return Node(allTrue, True, None, None, None, None)
        #topLeft
        mid = n // 2

        # use list comprehension and slicing to get the subgrids
        topleft = self.construct([row[:mid] for row in grid[:mid]])
        topright = self.construct([row[mid:] for row in grid[:mid]])
        bottomleft = self.construct([row[:mid] for row in grid[mid:]])
        bottomright = self.construct([row[mid:] for row in grid[mid:]])
        return Node(True, False, topleft, topright, bottomleft, bottomright) 
        


grid = []
for i in range(4):
  row = []

  for j in range(4):
    value = i * 4 + j

    row.append(value)

  grid.append(row)

print(Solution().construct(grid))



# @lc code=end

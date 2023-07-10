#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
# Definition for a Node.
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        q = deque([node])
        clones = {node.val: Node(node.val, [])}
        
        while q:
            curr = q.popleft()

            for neighbor in curr.neighbors:
                # check if neighbor has not been cloned, if not, clone it, add to map.
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)
                # connect this curr's clone to neighbor's cloneGraph
                clones[curr.val].neighbors.append(clones[neighbor.val])

        return clones[node.val]
        
# @lc code=end

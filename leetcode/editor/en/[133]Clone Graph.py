# leetcode submit region begin(Prohibit modification and deletion)

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                # if node has been cloned already, return the new, cloned, node.
                return oldToNew[node]
            # if it hasn't been cloned, create it
            copy = Node(node.val)
            oldToNew[node] = copy
            # go through each neighbor of the old node
            # run DFS on each neighbor
            for neighbor in node.neighbors:
                # the dfs returns the copy of that neighbor, append that to the clone's neighbor list.
                copy.neighbors.append(dfs(neighbor))

            return copy
        return dfs(node) if node else None

# leetcode submit region end(Prohibit modification and deletion)

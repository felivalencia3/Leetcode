# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        #RECURSIVE DFS
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # ITERATIVE BFS
        if not root:
            return 0

        level = 1
        q = collections.deque([root])
        # Usual iterative BFS
        # Each iteration of the while loop is a new level

        while q:
            # Process all nodes at current level of tree (add their children to the queue)
            # All old values of the q are removed and what's left is the new level of children,
            # if there is at least one, the level is increased and the loop goes again.
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1

        return level

        # ITERATIVE DFS
        # Use a stack to simulate call stack

        # we'll actually do preorder: root, left, right because its easier
        # for each node we'll add depth of node to stack, and return max depth.

        stack = [[root, 1]]  # stack holds node, depth
        res = 0
        # while stack is not empty
        while stack:
            node, depth = stack.pop()
            # grab node from the right side of the deque, so the last one that was put in.
            # if the node is not null, update res if this is at a lower level than seen before
            # and append the left and right nodes, knowing they are one level lower than this one.
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res
        """

# leetcode submit region end(Prohibit modification and deletion)

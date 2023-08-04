#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import Optional


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        # level order traversal
        queue = deque([root])
        result = []
        while queue:
            rightmost = None
            for _ in range(len(queue)):
                node = queue.popleft()
                rightmost = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(rightmost)


        return result


# @lc code=end
# Testcase: [1,2,3,4], in heap format, where parent is at index i, left child is at 2*i+1, right child is at 2*i+2
tree = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
print(Solution().rightSideView(tree))

#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import Optional
from collections import defaultdict, deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        # Iterative BFS with queue
        if not root:
            return []
        q = deque([(root, 1)])
        answer = defaultdict(list)
        while q:
            node, depth = q.popleft()

            answer[depth].append(node.val)
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        return list(answer.values())
# @lc code=end

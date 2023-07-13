#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = [k - 1, 0]
        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            if node.left is None and node.right is None:
                ans[1] = node.val
                ans[0] -= 1
                return
            # left, node, right
            inorder(node.left)
            if ans[0] == 0:
                return
            inorder(node.right)
        inorder(root)
        return ans[1]
# @lc code=end

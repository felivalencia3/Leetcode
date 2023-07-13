#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 0
        def r_goodNodes(node: TreeNode, curr_largest: int) -> None:
            nonlocal count
            if node is None:
                return
            if node.val >= curr_largest:
                count += 1
                curr_largest = node.val
            r_goodNodes(node.left, curr_largest)
            r_goodNodes(node.right, curr_largest)
            
        r_goodNodes(root, root.val)
        return count
# @lc code=end

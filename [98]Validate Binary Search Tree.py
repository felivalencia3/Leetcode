# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # a valid BST has: left child is smaller, right child is larger. repeat.
        # recursive, return False if there is ever an error (AND Logic)
        # when get to end, return True
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            # go left, update right boundary to curr and vice versa
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float("-inf"), float("inf"))

# leetcode submit region end(Prohibit modification and deletion)

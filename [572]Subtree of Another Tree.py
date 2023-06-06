# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case:
        if not subRoot:
            # Empty trees are subtrees of all trees
            return True
        if not root:
            # if root is empty and subRoot is not empty, return False
            return False

        # Check if root and subRoot Trees are equal
        if self.sameTree(root, subRoot):
            return True

        # If they are not equal, run isSubTree on L and R
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        else:
            return False

# leetcode submit region end(Prohibit modification and deletion)

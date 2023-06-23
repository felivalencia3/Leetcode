# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        # Heap Solution: O(n log n)
        result = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result[k - 1]
        """

        # Inorder traversal iteratively
        # Using a stack
        # Go as far left as possible. Add nodes you've passed to a stack (you'll go back to these).
        # When you reach null, start going back up stack.
        # the number of times you pop from the stack is k. k=1 is the first elem in stack, etc
        # for each of these, go right and add these to stack, then try to go left inside these.
        n = 0
        stack = []
        curr = root

        while curr and stack:
            # Go left as much as possible, add nodes visited to stack
            while curr:
                stack.append(curr)
                curr = curr.left

            # When we reached end of left-streak, go back up stack
            curr = stack.pop()
            n += 1  # Counter of how many nodes we've popped (this will equal k)
            if n == k:
                return curr.val
            # If n isn't k yet, move right, and try to go as left as possible again.
            curr = curr.right


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().kthSmallest(TreeNode(3), 1))

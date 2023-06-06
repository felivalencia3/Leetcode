# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import heapq
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def inorder(node: Optional[TreeNode]):
            if not node:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        heapq.heapify(result)

        # Perform k-1 extract-min operations
        for _ in range(k - 1):
            heapq.heappop(result)

        return heapq.heappop(result)


# leetcode submit region end(Prohibit modification and deletion)
# [3,1,4,null,2]
root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(Solution().kthSmallest(root, 2))

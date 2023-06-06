# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        # Each level is a state of the queue.
        if not root:
            return []

        res = []
        q = collections.deque([root])
        while q:
            res.append([node.val for node in q])
            for i in range(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

        return res


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().levelOrder(TreeNode(3)))

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, node: Optional[ListNode]) -> Optional[ListNode]:
        # Given head of SLL, reverse list and return head of new list.
        # Recursively and iteratively
        # 1) Iteratively
        """
        if not head or not head.next:
            return head

        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
        """

        # 2) Recursively
        # A Node class that represents a node in a linked list

        # A function that reverses a linked list recursively
        # Base case: if the node is None or the last node, return it as the new head
        if node is None or node.next is None:
            return node
        # Recursive case: reverse the next node and then make it point to the current node
        new_head = self.reverseList(node.next)
        node.next.next = node
        # Set the current node's next attribute to None
        node.next = None
        # Return the new head of the reversed list
        return new_head


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().reverseList(ListNode(1, ListNode(2, ListNode(3)))))

#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

def print_linked_list(head):
    linked_list_str = ""
    current_node = head

    while current_node:
        linked_list_str += str(current_node.val)
        linked_list_str += " -> "
        current_node = current_node.next

    print(linked_list_str)

def create_linked_list(arr):
    if not arr:
        return None
    
    head = ListNode(val=arr[0])
    current = head
    
    for val in arr[1:]:
        new_node = ListNode(val=val)
        current.next = new_node
        current = new_node
    
    current.end = True
    
    return head
# @lc code=start
# Definition for singly-linked list. 
from typing import Optional


class ListNode:
    def __init__(self, val=0, end=False, next=None):
        self.val = val
        self.next = next
        self.end = end


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        prev = None
        curr = head
        for _ in range(k):
            if curr is not None:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next

        head.next = self.reverseKGroup(curr, k)
        return prev
# @lc code=end
arr = [1, 2, 3, 4, 5]
linked_list = create_linked_list(arr)
new_head = Solution().reverseKGroup(linked_list, 2)
print_linked_list(new_head)

#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
from typing import List, Optional
import heapq


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        res = dummy
        counter = 0
        pq = []
        for node in lists:
            pq.append((node.val, counter, node))
            counter += 1
        heapq.heapify(pq)
        while pq:
            val, counter, e = heapq.heappop(pq)
            res.next = e
            res = res.next
            if e.next:
                heapq.heappush(pq, (e.next.val, counter, e.next))
                counter += 1
        return dummy.next


def print_linked_list(head):
    while head is not None and head.next is not None:
        print(head.val, end=" -> ")
        head = head.next
    if head is not None:
        print(head.val)


# @lc code=end
ll1 = ListNode(1, ListNode(4, ListNode(5)))
ll2 = ListNode(1, ListNode(3, ListNode(4)))
ll3 = ListNode(2, ListNode(6))
print_linked_list(Solution().mergeKLists([ll1, ll2, ll3]))

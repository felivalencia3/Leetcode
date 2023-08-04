#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return None
        copy = {}
        def recursive_copy(node: Node) -> Node:
            if node in copy:
                return copy[node]
            copy[node] = Node(node.val)
            if node.next:
                copy[node].next = recursive_copy(node.next)
            if node.random:
                copy[node].random = recursive_copy(node.random)
            return copy[node]
        # Make a deep copy of the linked list starting from head
        node = head
        while node:
            copy[node] = recursive_copy(node)
            node = node.next
        return copy[head]
# @lc code=end
# Convert this list into a linked list like defined above: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
head = Node(7).next = Node(13).next = Node(11).next = Node(10).next = Node(1)
print(Solution().copyRandomList(head))

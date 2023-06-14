from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # move one pointer n steps forward + 1, loop that until end alongside head.
    # when that pointer reaches end, slow will be at the node before nth.
    fast = head
    for i in range(n + 1):
        fast = fast.next
    slow = head
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove node after slow
    slow.next = None if not slow.next else slow.next.next
    return head


print_linked_list(
    removeNthFromEnd(
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), n=5
    )
)

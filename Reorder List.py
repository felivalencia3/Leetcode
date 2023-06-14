from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> ListNode:
    if not head:
        return head

    # Find the middle of the list
    slow, fast = head, head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Reverse the second half of the list
    prev = None
    curr = slow.next
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    slow.next = None

    # Merge the two halves
    dummy = ListNode()
    tail = dummy

    while head and prev:
        tail.next = head
        head = head.next
        tail = tail.next

        tail.next = prev
        prev = prev.next
        tail = tail.next

    tail.next = head or prev

    return dummy.next


def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    print(" -> ".join(values))


start = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print_linked_list(reorder_list(start))

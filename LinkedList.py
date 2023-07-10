from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value

    def get_value(self) -> int:
        return self.value
    
    def set_value(self, new_value: int) -> None:
        self.value = new_value

    def __str__(self) -> str:
        return str(self.value)

class LinkedListNode(Node):

    def __init__(self, value: int, next: Optional[Node] = None) -> None:
        super().__init__(value)
        self.next = next

    def get_next(self) -> Optional[Node]:
        return self.next

    def set_next(self, next: int) -> None:
        self.next = LinkedListNode(next)

class LinkedList:
    def __init__(self, head: Optional[LinkedListNode]) -> None:
        self.head = head








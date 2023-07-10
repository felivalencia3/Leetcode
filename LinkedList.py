from abc import ABC, abstractmethod
from typing import Optional


class Node(ABC):
    def __init__(self, value: int) -> None:
        self.value = value

    def get_value(self) -> int:
        return self.value

    def set_value(self, new_value: int) -> None:
        self.value = new_value

    @abstractmethod
    def __str__(self) -> str:
        pass


class LinkedListNode(Node):
    def __init__(self, value: int, next=None) -> None:
        super().__init__(value)
        self.next = next

    def __str__(self) -> str:
        return f"{self.value} ->"


class LinkedList:
    def __init__(self, head: LinkedListNode) -> None:
        self.head = head

    def append(self, value: int) -> None:
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node 
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

    def prepend(self, value: int) -> None:
        node = LinkedListNode(value, self.head)
        self.head = node

    def insert(self, index: int, value: int) -> None:
        curr = self.head
        for _ in range(index - 1):
            if curr.next is not None:
                curr = curr.next
            else:
                raise IndexError
        curr.next = LinkedListNode(value, curr.next)
    
    def remove(self, value: int) -> None:
        curr = self.head
        while curr.next is not None:
            if curr.next.value == value:
                # remove
                curr.next = curr.next.next
                return
            else:
                # move forward
                curr = curr.next
        raise ValueError

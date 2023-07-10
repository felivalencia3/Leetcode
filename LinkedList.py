from abc import ABC, abstractmethod
from typing import Optional


class Node(ABC):
    def __init__(self, value: int) -> None:
        self.value = value

    @abstractmethod
    def __str__(self) -> str:
        pass


class LinkedListNode(Node):
    def __init__(self, value: int, next=None) -> None:
        super().__init__(value)
        self.next = next

    def __str__(self) -> str:
        return f"{self.value} -> "


class LinkedList:
    def __init__(self, head: Optional[LinkedListNode] = None) -> None:
        self.head = head
        self.len = 0
        if head is not None:
            curr = head
            while curr:
                curr = curr.next
                self.len += 1

    def append(self, value: int) -> None:
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node 
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
            self.len += 1

    def prepend(self, value: int) -> None:
        node = LinkedListNode(value, self.head)
        self.head = node
        self.len += 1

    def insert(self, index: int, value: int) -> None:
        if index == 0:
            return self.prepend(value)
        if self.head is not None:
            curr = self.head
            for _ in range(index - 1):
                if curr.next is not None:
                    curr = curr.next
                else:
                    raise IndexError
            curr.next = LinkedListNode(value, curr.next)
            self.len += 1
    
    def remove(self, value: int) -> None:
        if self.head is not None:
            if self.head.value == value:
                self.head = self.head.next
                return
            curr = self.head
            while curr.next is not None:
                if curr.next.value == value:
                    # remove
                    curr.next = curr.next.next
                    self.len -= 1
                    return
                else:
                    # move forward
                    curr = curr.next
            raise ValueError
    
    def reverse(self) -> Optional[LinkedListNode]:
        prev, curr = None, self.head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev
        return prev

    def __str__(self) -> str:
        curr = self.head
        res = ""
        while curr:
            res += str(curr)
            curr = curr.next
        return res[:-3]

    def __len__(self) -> int:
        return self.len

    def is_palindrome(self) -> bool:
        # use a stack
        stack = []
        curr = self.head
        # add second half of elements to stack
        for i in range(self.len):
            curr = curr.next if curr is not None else None
            if i >= self.len // 2:
                stack.append(curr)
        curr = self.head
        for j in range(self.len//2):
            top = stack.pop()
            if curr is None:
                break
            if curr.value != top.value:
                return False
            curr = curr.next
        return True


if __name__ == "__main__":
    ll = LinkedList()
    # add 0 - 10 to list
    data = [1, 2, 3, 4, 4, 3, 2, 1]
    for i in data:
        ll.append(i)
    print(ll.is_palindrome())

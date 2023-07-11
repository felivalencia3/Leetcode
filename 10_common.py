#1. Valid Anagram
import collections
import heapq
from typing import Optional

def anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    return sorted(s1.lower()) == sorted(s2.lower())

def first_and_last(arr: list[int], target: int) -> list[int]:
    # O(log n)
    if not arr or not (arr[0] <= target <= arr[-1]):
        return [-1, -1]
    # do binary search twice.
    def find_start() -> int:
        if arr[0] == target:
            return 0
        l, r = 0, len(arr) - 1
        # Binary search
        while l < r:
            mid = (l + r) // 2
            # found first item
            if arr[mid] == target and arr[mid - 1] < target:
                return mid
            elif arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
    def find_end() -> int:
        if arr[-1] == target:
            return len(arr) - 1
        l, r = 0, len(arr) - 1
        
        while l < r:
            mid = (l + r) // 2
            if arr[mid] == target and arr[mid + 1] > target:
                return mid
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
    return [find_start() , find_end()]

# 3. Kth Largest Element
def klargest(arr: list[int], k: int) -> Optional[int]:
    if not arr or k > len(arr):
        return None
    # return k-th largest Element
    # first idea, use a maxHeap, pop k - 1 elems, then return pop of kth. O(k logn)
    min_heap = arr[:k]
    heapq.heapify(min_heap)

    for i in arr[k:]:
        if i > min_heap[0]:
            heapq.heapreplace(min_heap, i)

    return min_heap[0]

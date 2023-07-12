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

# Symmetric Tree Checker
class TreeNode:
    def __init__(self, value: int, left: "TreeNode", right: "TreeNode") -> None:
        self.value = value
        self.left = left
        self.right = right

def symmetric(root: TreeNode) -> bool:
    if root is None:
        return True
    def symmetric_helper(root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.value != root2.value:
            return False
        return symmetric_helper(root1.left, root2.right) and symmetric_helper(root1.right, root2.left)
    return symmetric_helper(root.left, root.right)

# Generate all the valid parentheses combinations
def parentheses(n: int) -> list[str]:
# recursive backtracking
# Base Case: when no more remaining open or closed
    combinations = []
    def backtrack(open_rem: int, closed_rem: int, path: str) -> None:
        if not open_rem and not closed_rem:
            combinations.append(path)
            return 
        # if you're not at end, try to go left or right (if you can go right) and append to path
        if open_rem:
            backtrack(open_rem - 1, closed_rem, path + "(")

        if open_rem < closed_rem and closed_rem:
            backtrack(open_rem, closed_rem - 1, path + ")")
    backtrack(n, n, "")
    return combinations

# find index of station where you can start and traverse all the way around without running out of gas.
def gas_station(gas: list[int], cost: list[int]) -> int:
    # post fix sum of diff
    diff = [gas[i] - cost[i] for i in range(len(gas))]
    if sum(diff) < 0:
        return -1
    post = [0] * len(gas)
    post[-1] = diff[-1]
    maxPost = post[-1] 
    maxIndex = len(gas) - 1
    for i in range(len(gas) - 2, -1, -1):
        post_sum = post[i + 1] + diff[i]
        post[i] = post_sum
        if post_sum > maxPost:
            maxPost = post_sum
            maxIndex = i
    return maxIndex 
def opti_gas_station(gas, cost):
        net = [g - c for g, c in zip(gas, cost)]
        if sum(net) < 0:
            return -1
        max_post_sum = 0
        max_index = 0
        curr_post_sum = 0
        for i in range(len(net) - 1, -1, -1):
            curr_post_sum += net[i]
            if curr_post_sum > max_post_sum:
                max_post_sum = curr_post_sum
                max_index = i
        return max_index

print(gas_station(gas = [1,2,3,4,5], cost = [3,4,5,1,2]))
print(gas_station([2,3,4], [3,4,3]))
print(gas_station([3,3,4], [3,4,4]))
print(gas_station([5,1,2,3,4], [4,4,1,5,1]))






















# leetcode submit region begin(Prohibit modification and deletion)
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # create minheap size k
        self.minHeap, self.k = nums, k
        # Heapify
        heapq.heapify(self.minHeap)
        # pop excess elements until size k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Add value to heap
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            # Pop smallest value of heap
            heapq.heappop(self.minHeap)

        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# leetcode submit region end(Prohibit modification and deletion)

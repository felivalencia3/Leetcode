

# leetcode submit region begin(Prohibit modification and deletion)
import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        return 0 if not stones else abs(stones[0])
        
# leetcode submit region end(Prohibit modification and deletion)

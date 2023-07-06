#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        freq_tuples = [(tup[1] * -1, tup[0]) for tup in frequencies.items()]
        heapq.heapify(freq_tuples)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(freq_tuples)[1])
        return res

# @lc code=end
print(Solution().topKFrequent([1], 1))

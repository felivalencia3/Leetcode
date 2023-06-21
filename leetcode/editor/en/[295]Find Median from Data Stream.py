# The median is the middle value in an ordered integer list. If the size of the 
# list is even, there is no middle value, and the median is the mean of the two 
# middle values. 
# 
#  
#  For example, for arr = [2,3,4], the median is 3. 
#  For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5. 
#  
# 
#  Implement the MedianFinder class: 
# 
#  
#  MedianFinder() initializes the MedianFinder object. 
#  void addNum(int num) adds the integer num from the data stream to the data 
# structure. 
#  double findMedian() returns the median of all elements so far. Answers 
# within 10⁻⁵ of the actual answer will be accepted. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]
# 
# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
#  
# 
#  
#  Constraints: 
# 
#  
#  -10⁵ <= num <= 10⁵ 
#  There will be at least one element in the data structure before calling 
# findMedian. 
#  At most 5 * 10⁴ calls will be made to addNum and findMedian. 
#  
# 
#  
#  Follow up: 
# 
#  
#  If all integer numbers from the stream are in the range [0, 100], how would 
# you optimize your solution? 
#  If 99% of all integer numbers from the stream are in the range [0, 100], how 
# would you optimize your solution? 
#  
# 
#  Related Topics Two Pointers Design Sorting Heap (Priority Queue) Data Stream 
# 👍 10446 👎 204
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # try to add to small, check if diff is > 1
        heapq.heappush(self.small, num * -1)
        if self.large:
            if self.large and self.small[0] * -1 > self.large[0]:
                over = heapq.heappop(self.small)
                heapq.heappush(self.large, over * -1)
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, heapq.heappop(self.small) * -1)
        elif len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, heapq.heappop(self.large) * -1)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            left = self.small[0] * -1
            right = self.large[0]
            return (left + right) / 2
        else:
            if len(self.small) > len(self.large):
                return self.small[0] * -1
            return self.large[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)

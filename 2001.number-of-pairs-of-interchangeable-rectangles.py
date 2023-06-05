#
# @lc app=leetcode id=2001 lang=python
#
# [2001] Number of Pairs of Interchangeable Rectangles
#

# @lc code=start
class Solution(object):
    def interchangeableRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        count = {}
        for w, h in rectangles:
            ratio = float(w) / float(h)  
            count[ratio] = 1 + count.get(ratio, 0)

        res = 0
        for c in count.values():
            if c > 1:
                res += (c * (c - 1)) // 2

        return res
    
# @lc code=end
rec = [[4,5],[7,8]]
print(Solution().interchangeableRectangles(rec))

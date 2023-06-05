#
# @lc app=leetcode id=122 lang=python
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        l, r = 0, 1
        curprofit = 0
        while r < len(prices):
            profit = prices[r] - prices[l]
            if profit > 0:
                curprofit = max(curprofit, profit)
                if r < len(prices)-1 and prices[r+1] < prices[r]:
                    total += curprofit
                    curprofit = 0
                    l = r
            else:
                l = r
            r += 1
        total += curprofit
        return total
        
# @lc code=end
test = [1,2,3,4,5]
print(Solution().maxProfit(test))

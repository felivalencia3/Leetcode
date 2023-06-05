#
# @lc app=leetcode id=2002 lang=python
#
# [2002] Maximum Product of the Length of Two Palindromic Subsequences
#

# @lc code=start
class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        palimap = dict()
        res = 0
        for mask in range(1, 1 << n):
            subseq = ""
            for i in range(n):
                if mask & (1 << i):
                    subseq += s[i]
                if subseq == subseq[::-1]:
                    palimap[mask] = len(subseq)
            
            for m1 in palimap:
                for m2 in palimap:
                    if m1 & m2 == 0:
                        res = max(res, palimap[m1] * palimap[m2])
        return res
            
                
            
        
# @lc code=end


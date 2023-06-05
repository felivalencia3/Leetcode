#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # l pointer loops left to right
        # move until h[l] == n[0]
        # initialize new pointer, scan along length of needle
        # if there is a mismatch, l = r, ignore r.
        # if there is no mismatch, return l.
        l, r = 0, 0
        while l < len(haystack):

            
            
        
# @lc code=end


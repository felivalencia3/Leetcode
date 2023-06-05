#
# @lc app=leetcode id=438 lang=python
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        m = len(p)
        
        p = Counter(p)                    # Convert list of anagram letters to a Counter (hashtable)
        ans = []
           
        window = None
        for i in range(0,n-m+1):
            if i == 0: 
                window = Counter(s[:m])   # Initialize window with beginning of s => length = length of anagram letters
            else:    
                window[s[i-1]] -= 1       # Move window to right: 1. remove character on the left
                window[s[i+m-1]] += 1     #                       2. add character on the right
            if len(window - p) == 0:      # Check if window is anagram (direct comparison of counters does not work with 0 entries)
                ans.append(i)
                
        return ans
        
# @lc code=end
s = "cbaebabacd"
p = "abc"
print(Counter(s[:len(p)]))
print(Solution().findAnagrams(s,p))

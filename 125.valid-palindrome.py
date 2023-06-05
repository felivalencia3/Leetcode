#
# @lc app=leetcode id=125 lang=python
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # convert all letters to lower, remove any alphanumeric
        s = [char.lower() for char in s if char.isalnum()]
        
        for i in range(0, len(s)//2):
            if s[i] != s[-i-1]:
                return False
        return True
        
# @lc code=end
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
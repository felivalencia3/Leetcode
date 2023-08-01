#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if not stack or temp <= stack[-1][0]:
                stack.append((temp, i))
            else:
                while True:
                    if not stack or stack[-1][0] >= temp:
                        stack.append((temp, i))
                        break
                    else:
                        _, idx = stack.pop()
                        res[idx] = i - idx 
        return res

        
# @lc code=end
print(Solution().dailyTemperatures(temperatures = [30,60,90]))

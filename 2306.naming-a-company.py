#
# @lc app=leetcode id=2306 lang=python3
#
# [2306] Naming a Company
#

# @lc code=start
class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        idea_set = set()
        res = 0
        for i in range(len(ideas)):
            for j in range(i + 1, len(ideas)):
                # swap first letters of ideas[i] and ideas[j]
                idea_set.add(ideas[i])
                idea_set.add(ideas[j])
                new1 = ideas[j][0] + ideas[i][1:]
                new2 = ideas[i][0] + ideas[j][1:]
                if new1 not in idea_set and new2 not in idea_set:
                    res += 2
        return res
# @lc code=end
print(Solution().distinctNames(ideas = ["coffee","donuts","time","toffee"]))

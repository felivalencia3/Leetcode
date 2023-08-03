#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start


from collections import defaultdict, deque
from bisect import insort


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        choices: dict[str, list] = defaultdict(list)
        for ticket in tickets:
            insort(choices[ticket[0]], ticket[1])
            if ticket[1] not in choices:
                choices[ticket[1]] = list()
        def dfs(path: list[str]) -> list[str]:
            if len(path) == len(tickets) + 1:
                return path

            for i, choice in enumerate(choices[path[-1]]):
                removed = choices[path[-1]].pop(i)
                itinerary_str = dfs(path + [choice])
                choices[path[-1]].insert(i, removed)
                if itinerary_str:
                    return itinerary_str
            return []
        
        return dfs(["JFK"])


# @lc code=end
print(Solution().findItinerary(
        [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
));

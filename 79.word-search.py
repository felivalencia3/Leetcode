#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Iterative DFS
        # Neighbors will be (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
        # Only traverse neighbors not in visited and that are the next letter that follow
        # Keep counter of idx in word, reset each time we can't find a neighbor to go to.
        # when index == len(word), return True
        # if we reach i == len(board) and j == len(board[0]) return False

        def traverse(pos: Tuple[int, int]):
            

        idx = 0
        for i in range(len(board)):
            for j in range(len(board)):
        
# @lc code=end


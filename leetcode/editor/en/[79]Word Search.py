from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Attempt at backtracking
        # List of choices made
        path = []

        def backtrack_exists(path: List, choices: List) -> bool:
            # check if all words in path are == word
            if [board[i][j] for i, j in path] == list(word):
                return True

            # recursively try different valid choices for next step in path
            for choice in choices:
                # choices are [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                # check if next choice is valid
                # i.e
                if :

# leetcode submit region end(Prohibit modification and deletion)

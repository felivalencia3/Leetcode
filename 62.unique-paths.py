#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
def print_matrix(mat: list[list]) -> None:
    for row in mat:
        for col in row:
            spaces = 3 #adjust as needed
            print(col, end = " " * spaces)
        print()

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 if i < n - 1 else 1 for i in range(n)] for _ in range(m - 1)]
        dp.append([1] * n)
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        
        return dp[0][0]
# @lc code=end
print(Solution().uniquePaths(3,3))

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        dp = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = i
        for j in range(m):
            dp[0][j] = j
        for i in range(1, n):
            for j in range(1, m):
                diff = 1 if word1[i] == word2[j] else 0
                dp[i][j] = min(1 + dp[i - 1][j], 1 + dp[i][j - 1], diff + dp[i - 1][j - 1])
        return dp[-1][-1] + 1
        
print(Solution().minDistance("horse", "ros"))



class Solution:
    def memo_climbStairs(self, n: int, memo: dict={}) -> int:
        if n in memo:
            return memo[n]
        if n in {0, 1}:
            return 1
        res = self.memo_climbStairs(n - 1) + self.memo_climbStairs(n - 2)
        memo[n] = res
        return res
    
    def tab_climbStairs(self, n: int) -> int:
        dp = [-1] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp.pop()
    
    # There's no need to keep track of the whole list, just the last two numbers, so
    def climbStairs(self, n: int) -> int:
        prev2 = 1
        prev1 = 1
        for i in range(1, n):
            # set current to the previous two
            curr = prev1 + prev2
            # move prev2 to prev1, move it forward by one index
            prev2 = prev1
            # move prev1 by one index, make it equal to curr. now its prev2 -> prev1 -> (next i)
            prev1 = curr
        return prev1

    
print(Solution().memo_climbStairs(80))
print(Solution().tab_climbStairs(80))
print(Solution().climbStairs(80))
import time
#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if not amount:
            return 0
        def memo_coinChange(curr: int, memo: dict={}) -> int:
            if curr in memo:
                return memo[curr]
            if curr == amount:
                return 0
            if curr > amount: 
                return -1
            values = [memo_coinChange(curr + coin, memo) for coin in coins]
            values = [value for value in values if value != -1]
            res = min(values) + 1 if values else -1
            memo[curr] = res
            return res

        def iter_coinChange() -> int:
            dp = [0] * (amount + 1)
            dp[0] = 0
            for i in range(1, amount + 1):
                values = [dp[i - coin] for coin in coins if i - coin >= 0 and dp[i - coin] != -1]
                dp[i] = min(values) + 1 if values else -1
            return dp[-1]

        return iter_coinChange()
        
# @lc code=end
start = time.time()
print(Solution().coinChange([1, 2, 5], 11))
end = time.time()
print(f"Time taken: {end - start} seconds")

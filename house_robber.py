import time
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        def memo_rob(nums: list[int], i: int, memo: dict={}) -> int:
            if i < 0:
                return 0
            
            if i in memo:
                return memo[i]
            
            res = max(memo_rob(nums, i - 2, memo) + nums[i], memo_rob(nums, i - 1))
            memo[i] = res
            return res
        
        def iter_rob(nums: list[int]) -> int:
            dp = [0] * n
            dp[n - 1] = nums[n - 1]
            dp[n - 2] = nums[n - 2]
            for i in range(n - 3, -1, -1):
                dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
            return dp[0]
        
        def opti_rob(nums: list[int]) -> int:
            if not nums:
                return 0
            prev1 = 0
            prev2 = 0
            # Forward Loop
            for num in nums:
                tmp = prev1
                prev1 = max(prev2 + num, prev1)
                prev2 = tmp
            return prev1

        return opti_rob(nums)
            

test = [226,174,214,16,218,48,153,131,128,17,157,142,88,43,37,157,43,221,191,68,206,23,225,82,54,118,111,46,80,49,245,63,25,194,72,80,143,55,209,18,55,122,65,66,177,101,63,201,172,130,103,225,142,46,86,185,62,138,212,192,125,77,223,188,99,228,90,25,193,211,84,239,119,234,85,83,123,120,131,203,219,10,82,35,120,180,249,106,37,169,225,54,103,55,166,124]
start = time.time()
print(Solution().rob(test))
end = time.time()
print(end - start)
# Answer: 7102
# Recursive Time: WAY TOO SLOW, never finished
# Memo Time: 0.00010538101196289062 -> e04
# Iter Time: 2.8848648071289062e-05 --> one order of magintude faster
# Iter N-Variables Time: 2.7418136596679688e-05 --> basically the same as tabulation

def containsSum(nums, t):
    n = len(nums)
    dp = [[False for _ in range(t + 1)] for _ in range(n + 1)]
    for row in range(n):
        dp[row][0] = True
    
    for i in range(1, n):
        for j in range(1, t + 1):
            if j >= nums[i - 1]:
                dp[i][j] = dp[i - 1][j - nums[i]] or dp[i - 1][j] or dp[i][j - nums[i]]
    return dp[n - 1][t]

nums = [3,5,4]
print(containsSum(nums, 19))

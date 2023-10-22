import time

def rob(nums):
    return rob_helper(nums, 0)

def rob_helper(nums, i):
    if i >= len(nums):
        return 0
    return max(nums[i] + rob_helper(nums, i+2), rob_helper(nums, i+1))

def rob_memo(nums):
    memo = [-1] * len(nums)
    return rob_helper_memo(nums, 0, memo)

def rob_helper_memo(nums, i, memo):
    if i >= len(nums):
        return 0
    if memo[i] != -1:
        return memo[i]
    memo[i] = max(nums[i] + rob_helper_memo(nums, i+2, memo), rob_helper_memo(nums, i+1, memo))
    return memo[i]

nums = [523,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]

# Without memoization
start = time.time()
rob(nums)
end = time.time()
print(f"Without memoization: {end - start:.6f} seconds")

# With memoization
start = time.time()
rob_memo(nums)
end = time.time()
print(f"With memoization: {end - start:.6f} seconds")


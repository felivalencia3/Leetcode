def minUniquePaths(nums):
    m = len(nums)
    n = len(nums[0])
    T = [[float("inf") for _ in range(n)] for _ in range(m)]
    T[0][0] = nums[0][0]
    for i in range(1, m):
        T[i][0] = T[i - 1][0] + nums[i][0]
    for j in range(1, n):
        T[0][j] = T[0][j - 1] + nums[0][j]

    for i in range(1, m):
        for j in range(1, n):
            T[i][j] = min(T[i - 1][j] + nums[i - 1][j], T[i][j - 1] + nums[i][j - 1])

    return T[-1][-1]

nums = [[2,1,4], [1,3,5], [9, 0, 1]]
print(minUniquePaths(nums))

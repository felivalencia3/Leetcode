arr = [1,2,3,4]
n = len(arr)
M = 3
res = []

def find_subsequences(arr, index, m):
    # find subsequence of length m of array arr
    if m == 0:
        res.append(arr[:index])
        return
    # recursion
    for i in range(index, n):
        find_subsequences(arr, i+1, m-1)

        

find_subsequences(arr, 0, M)
print(res)
    





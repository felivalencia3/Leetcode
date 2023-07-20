class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:        
        # implement merge sort.
        # first split then merge
        def mergeSort(nums: list[int]) -> None:
                l = len(nums)
                if l > 1:
                    m = l // 2
                    L = nums[:m]
                    R = nums[m:]
                    mergeSort(L)
                    mergeSort(R)
                    
                    # merge two sorted list
                    i = j = k = 0
                    while i < len(L) and j < len(R):
                        if L[i] < R[j]:
                            nums[k] = L[i]
                            i += 1
                        else:
                            nums[k] = R[j]
                            j += 1
                        k += 1
                    nums[k:] = L[i:] + R[j:]
        mergeSort(nums)
        return nums

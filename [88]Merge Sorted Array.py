# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        def shift(k):
            last = nums1[k]
            while nums1[k] != 0:
                temp = nums1[k + 1]
                nums1[k + 1] = last
                last = temp
                k += 1

        i, j = 0, 0

        while j < n:
            if i >= n:
                nums1[i:] = nums2[j:]
                break
            if nums2[j] < nums1[i]:
                shift(i)
                i += 1
                nums1[i] = nums2[j]
                j += 1
            else:
                i += 1

    def removeDuplicates(self, nums: List[int]) -> (List[int], int):
        if len(nums) == 0:
            return 0
        l = 1
        inc = False
        for r in range(1, len(nums)):
            if nums[r] == nums[r - 1]:
                l = l + 1 if not inc else l
                inc = True
            else:
                nums[l] = nums[r]
                inc = False
                l += 1
        if inc:
            nums[l - 1] = nums[r]
        return nums, l


# leetcode submit region end(Prohibit modification and deletion)
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]

nums, k = Solution().removeDuplicates(nums)
print(nums[:k])

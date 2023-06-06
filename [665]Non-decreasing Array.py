# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False

        for i in range(len(nums) - 1):
            if nums[i] <= nums[i+1]:
                continue
            if changed:
                return False

            # decrease left element if possible
            if i == 0 or nums[i + 1] >= nums[i-1]:
                nums[i] = nums[i+1]
            else:
                nums[i + 1] = nums[i]
            changed = True
        return True




# leetcode submit region end(Prohibit modification and deletion)
nums = [5,7,1,8]
print(Solution().checkPossibility(nums))

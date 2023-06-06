

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, res = set(), set()

        for l in range(len(s)-9):
            cur = s[l:l+10]
            if cur in seen:
                res.add(cur)
            else:
                seen.add(cur)
        return sorted(list(res))





        
# leetcode submit region end(Prohibit modification and deletion)

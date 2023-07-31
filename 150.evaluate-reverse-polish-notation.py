#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        # add tokens to stack
        # when you find an operand, pop last two, apply, and return result to stack.
        stack = []
        for token in tokens:
            if token in ("+", "-", "*", "/"):
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(int(eval(f"{num2} {token} {num1}")))
            else:
                stack.append(int(token))
        return stack[0]
        
# @lc code=end
print(Solution().evalRPN(["4"]))

#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        return self.s1(s)

    def s1(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            c = s[i]
            if stack:
                last = stack[len(stack)-1]
                if self.is_match(last, c):
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        if stack:
            return False
        return True
    
    def is_match(self, s1, s2):
        if s1 == '(' and s2 == ')' or s1 == '{' and s2 == '}' or s1 == '[' and s2 == ']':
            return True
        return False
# @lc code=end


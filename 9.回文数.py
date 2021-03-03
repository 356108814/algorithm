#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        return x == self.reverseNum(x)

    def reverseNum(self, x: int) -> int:
        res = 0
        while x != 0:
            r = x % 10
            x = x // 10
            res = res * 10 + r
        return res

    def isPalindrome2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]

if __name__ == '__main__':
    s = Solution()
    print(s.reverseNum(123))
# @lc code=end


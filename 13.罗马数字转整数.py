#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        如果当前字符的值小于后一个字符的值，则需要减去当前值，如IV = -1 + 5。
        否则直接相加即可
        """
        ans = 0
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        size = len(s)
        for i in range(len(s)):
            v = d[s[i]]
            if i != size - 1 and v < d[s[i+1]]:
                ans -= v
            else:
                ans += v
        return ans


# @lc code=end


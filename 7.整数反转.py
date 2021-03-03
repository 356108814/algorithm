#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        """
        1.数值范围
        2.python中//向下取整
        3.负数%问题，-123 % 10 结果为7，而不是3
        """
        # -2147483648 < x < 2147483647
        min_value = -pow(2, 31)
        max_value = pow(2, 31) - 1
        absx = abs(x)
        res = 0
        while absx != 0:
            pop = absx % 10
            # // 为向下取整
            absx = absx // 10
            res = res * 10 + pop
        res = res if x > 0 else -res
        if res < min_value or res > max_value:
            return 0
        else:
            return res

    def reverse2(self, x: int) -> int:
        """字符串转换"""
        s = str(x)
        if x < 0:
            n = int('-' + s[1:][::-1])
        else:
            n = int(s[::-1])

        if n < -pow(2, 31) or n > pow(2, 31) - 1 or n == 0:
            return 0
        return n


if __name__ == "__main__":
    # print(-pow(2, 31))
    # print(pow(2, 31))
    print(-123 % 10)
    pass


# @lc code=end

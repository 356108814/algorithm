#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
from typing import List

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        只有一个数字出现1次，其他的都是出现3次。因为需要设计一个算法，使一个数计算3次后为0，那剩下的数即为只出现一次的数字。
        """
        a = b = 0
        for x in nums:
            b = (b ^ x) & ~a
            a = (a ^ x) & ~b
        return b


if __name__ == '__main__':
    l = [7, 7, 7, 2]
    s = Solution()
    print(s.singleNumber(l))

# @lc code=end


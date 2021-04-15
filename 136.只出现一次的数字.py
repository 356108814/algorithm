#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return self.s1(nums)

    def s1(self, nums: List[int]) -> int:
        """
        异或运算满足交换律和结合律，a^b^a = a^a^b = b
        因此数字全部异或后的结果就为只出现一次的数
        """
        ans = nums[0]
        is_first = True    # 注意计算时第一个数不要重复计算
        for x in nums:
            if not is_first:
                ans = ans ^ x
            is_first = False
        return ans

    def s2(self, nums: List[int]) -> int:
        """字典记录次数"""
        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        for x in d:
            if d[x] == 1:
                return x

# @lc code=end


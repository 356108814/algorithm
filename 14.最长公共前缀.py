#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.s2(strs)

    def s1(self, strs: List[str]) -> str:
        prefix = ''
        if strs:
            first = strs[0]
            for i in range(len(first)):
                char = first[i]
                is_diff = False
                for j in range(1, len(strs), 1):
                    s = strs[j]
                    if i >= len(s) or char != s[i]:
                        is_diff = True
                        break
                if is_diff:
                    break
                else:
                    prefix += char
        return prefix

# @lc code=end

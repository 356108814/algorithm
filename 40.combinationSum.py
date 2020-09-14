# coding:utf-8

# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的每个数字在每个组合中只能使用一次。

# 说明：

# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
# 示例 1:

# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()
        self.backtrack(candidates, 0, target, path, res)
        return res

    def backtrack(self, candidates, start, residue, path, res):
        if residue == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > residue:
                continue
            if i > start and candidates[i - 1] == candidates[i]:    # 数字已排序去重
                continue
            path.append(candidates[i])
            self.backtrack(candidates, i + 1, residue - candidates[i], path, res)
            path.pop()




if __name__ == '__main__':
    solution = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(solution.combinationSum2(candidates, target))
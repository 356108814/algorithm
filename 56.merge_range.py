# coding: utf-8
# 56 合并区间
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。

# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        dist = []
        length = len(intervals)
        i = 0
        while i < length:
            a = intervals[i]
            can_merge = False
            for j in range(i + 1, length):
                b = intervals[j]
                if a[0] >= b[0] and a[0] <= b[1]:
                    # 可合并
                    dist.append([b[0], a[1]])
                    can_merge = True
                    break
                elif b[0] >= a[0] and b[0] <= a[1]:
                    dist.append([a[0], b[1]])
                    can_merge = True
                    break
                else:
                    pass
            if not can_merge:
                dist.append(a)
                i += 1
            else:
                i = j + 1
        return dist


if __name__ == '__main__':
    solution = Solution()
    source = [[1,4],[1,5]]
    # source =[[1,3],[2,6],[8,10],[15,18]]
    print(solution.merge(source))

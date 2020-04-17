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
        # 先按元素升序排序
        intervals.sort(key = lambda x: x[0])
        for interval in intervals:
            # dist的最后一个元素的右端点 < interval左端点，即不会重合，直接加入目标dist
            if not dist or dist[-1][1] < interval[0]:
                dist.append(interval)
            else:
                dist[-1][1] = max(dist[-1][1], interval[1])
        return dist


if __name__ == '__main__':
    solution = Solution()
    source = [[1,4],[1,5]]
    # source =[[1,3],[2,6],[8,10],[15,18]]
    print(solution.merge(source))

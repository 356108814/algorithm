# coding: utf-8
# 542 01矩阵
from typing import List

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        # 行数
        m = len(matrix)
        # 列数
        n = len(matrix[0])
        # 将所有为0的元素加入待访问队列
        q = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    print(i, j)
                    q.append((i, j))
                else:
                    # 将所有为1的设置为-1，表示为未访问的
                    matrix[i][j] = -1
        print(matrix)
        # print(q)

        # BFS广度优先遍历
        while len(q):
            i, j = q.pop(0)
            print(i, j)
            # 处理(i, j)的上(i - 1, j)、下(i + 1, j)、左(i, j- 1)、右(i, j + 1)的元素，值为当前元素值+1
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                # 元素有效且未访问过
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] == -1:
                    matrix[ni][nj] = matrix[i][j] + 1
                    print(ni, nj)
        return matrix


if __name__ == '__main__':
    solution = Solution()
    matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    print(solution.updateMatrix(matrix))

    # for i in range(3):
    #         for j in range(3):
    #             # print(i, j)
    #             print(matrix[i][j])

# coding: utf-8
class Solution:
    def rotate(self, matrix) -> None:
        result = []
        n = len(matrix)
        # 初始化空矩阵
        for x in range(n):
            result.append([])
        
        for i, rv in enumerate(matrix):
            for j, cv in enumerate(rv):
                result[j].insert(0, cv)
        matrix = result
        print(matrix)

    def rotate2(self, matrix) -> None:
        for i, rv in enumerate(matrix):
            for j, cv in enumerate(rv):
                pass


if __name__ == '__main__':
    s = Solution()
    matrix = [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
    matrix = [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ]
    s.rotate(matrix)

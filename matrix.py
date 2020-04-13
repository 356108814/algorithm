# coding: utf-8
class Solution:
    def rotate(self, matrix) -> None:
        """思路：matrix_new[col][n - row - 1] = matrix[row][col]"""
        matrix_new = []
        n = len(matrix)
        # 初始化空矩阵
        for x in range(n):
            matrix_new.append([])
        
        for i, rv in enumerate(matrix):
            for j, cv in enumerate(rv):
                matrix_new[j].insert(0, cv)
        matrix[:] = matrix_new

    def rotate2(self, matrix) -> None:
        """
        思路：元素按圈顺时针旋转，如：1、11、16、15一个圈，1、10、12、13一个圈
        关键等式：matrix_new[col][n-row-1] = matrix[row][col]
        1. 
        temp = matrix[col][n-row-1]
        matrix[col][n-row-1] = matrix[row][col]

        将row=col,col=n-row-1代入关键等式
        matrix[n-row-1][n-col-1] = matrix[col][n-row-1]
        2.
        temp = matrix[n-row-1][n-col-1]
        matrix[n-row-1][n-col-1] = matrix[col][n-row-1]
        将row=n-row-1,col=n-col-1,代入关键等式
        matrix[n-col-1][row] = matrix[n-row-1][n-col-1]
        3.
        matrix[col][n-row-1] = temp
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
              temp = matrix[i][j]
              matrix[i][j] = matrix[n - j - 1][i]
              matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
              matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
              matrix[j][n - i - 1] = temp
                


if __name__ == '__main__':
    s = Solution()
    matrix = [
      [1,2,3],  # [7, 4, 1]
      [4,5,6],  # [8, 5, 2]
      [7,8,9]   # [9, 6, 3]
    ]
    matrix = [
      [ 5, 1, 9,11], # [15, 13,  2,  5]
      [ 2, 4, 8,10], # [14,  3,  4,  1]
      [13, 3, 6, 7], # [12,  6,  8,  9]
      [15,14,12,16]  # [16,  7, 10, 11]
    ]
    s.rotate2(matrix)
    print(matrix)

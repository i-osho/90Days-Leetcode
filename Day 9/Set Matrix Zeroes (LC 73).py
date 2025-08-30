class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        loc = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    loc.append((i, j))
        for i, j in loc:
            for k in range(len(matrix)):
                matrix[k][j] = 0
            for k in range(len(matrix[0])):
                matrix[i][k] = 0
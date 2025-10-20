class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows , cols = [] , []
        for i in range(0, len(matrix)):
            for j in range(0 , len(matrix[0])):
                if(matrix[i][j] == 0):
                    rows.append(i)
                    cols.append(j)

        for row , col in zip(rows, cols):
            for i in range(0 , len(matrix[0])):
                matrix[row][i]  = 0
            for j in range(0 , len(matrix)):
                for j in range(0 , len(matrix)):
                    matrix[j][col] = 0
        return(matrix)
                
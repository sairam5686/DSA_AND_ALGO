class Solution(object):
    def setZeroes(self, matrix):
        cols , rows = [] , []
        for col in range(len(matrix)):
            for row in range(len(matrix[0])):
                if(matrix[col][row] == 0 ):
                    cols.append(col)
                    rows.append(row)

        for i , j in zip(cols , rows):
            for row in range(len(matrix[0])):
                matrix[i][row] =  0

            for col in range(len(matrix)):
                matrix[col][j] = 0
                
        return (matrix)
                
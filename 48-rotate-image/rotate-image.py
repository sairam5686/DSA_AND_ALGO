class Solution(object):
    def rotate(self, matrix):
        for i in range(len(matrix)):
            for j in range(i+1 , len(matrix[0])):
                matrix[i][j]  , matrix[j][i] = matrix[j][i] , matrix[i][j]
        for row in range(len(matrix)):
            rev_row = matrix[row][::-1]
            matrix[row] = rev_row
        return(matrix)
                
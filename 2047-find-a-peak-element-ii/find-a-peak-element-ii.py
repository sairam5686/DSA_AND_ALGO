class Solution(object):
    def findPeakGrid(self, mat):
        result = []
        maxs = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if(mat[i][j] > maxs):
                    result = [i,j]
                    maxs = max(maxs , mat[i][j])
        return(result)
                
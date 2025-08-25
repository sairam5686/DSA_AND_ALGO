def getdiagrnal(source_row , source_col , row , col , mat ):
    dummy = []
    while source_row<row and source_col>=0:
        dummy.append(mat[source_row][source_col])
        source_col -=1
        source_row +=1
    return dummy
class Solution(object):
    def findDiagonalOrder(self, mat):
        row , col =  len(mat) , len(mat[0])
        result = []
        for j in range(0 , col):
            intermediate  = getdiagrnal(0 , j , row , col , mat)
            if( j %2 == 0 ):
                intermediate.reverse()
            result.extend(intermediate)

        for i in range(1 ,row):
            intermediate = getdiagrnal(i,col-1 , row, col, mat)
            if((i+col-1 )%2 == 0 ):
                intermediate.reverse()
            result.extend(intermediate)
        return(result)
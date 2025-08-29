def row_max(mat , col):
    result , index = 0 ,0
    for i in range( len(mat)):
        if(mat[i][col] > result):
            result =  mat[i][col]
            index = i
    return index

class Solution(object):
    def findPeakGrid(self, mat):
        low  , high = 0 , len(mat[0])-1
        left , right = -1 ,-1

        while(low <=high):
            mid = (low + high)//2
            row=row_max(mat , mid)

            if(mid-1<0 ):
                left  = -1
            else:
                left = mat[row][mid-1]

            if (mid +1> len(mat[0])-1):
                right = -1
            else:
                right= mat[row][mid+1]

            if(mat[row][mid]>left and mat[row][mid]>right):
                return([row,mid])
              
            elif(mat[row][mid]< left):
                high = mid -1
            else:
                low = mid + 1
        return([-1,-1])
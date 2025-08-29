class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col_length  = len(matrix[0])-1
        
        for i in range(len(matrix)):
            if(matrix[i][0]<= target and matrix[i][col_length] >= target):
                low , high = 0 , col_length
                while(low <= high):
                    mid = (low + high) // 2
                    if(matrix[i][mid] == target):
                        return(True)
                        break
                    elif(matrix[i][mid]> target):
                        high = mid-1
                    else:
                        low = mid + 1
            else:
                continue
        return False
                        
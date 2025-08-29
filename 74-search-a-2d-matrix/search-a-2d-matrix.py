class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length  = len(matrix) * len(matrix[0])-1
        low , high = 0 , length
        while(low <= high ):
            mid = ((low + high) // 2)
            convertor_row ,convertor_col = mid // len(matrix[0]) , mid % len(matrix[0])
            if(matrix[convertor_row][convertor_col] == target):
                return(True)
                
            elif(matrix[convertor_row][convertor_col] > target):
                high  = mid -1
            else:
                low = mid + 1
        return(False)
                
class Solution:
    def findRotation(self, matrix: List[List[int]], target: List[List[int]]) -> bool:
  
        for  i in range(4):
            for i in range(0 , len(matrix)):
                for j in range(i+1 , len(matrix[0])):
                    matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]

            for i in range(len(matrix)):
                matrix[i].reverse()
            if(matrix == target):
                return True
        return False
            
        

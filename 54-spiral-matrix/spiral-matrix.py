class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        left =  0
        right  = len(matrix[0])
        top  = 0
        bottom = len(matrix)
        res = []
        while(top < bottom and left<right):
            for i in range(left , right):
                print(top ,  i)
                res.append(matrix[top][i])

            top +=1
            for i in range(top , bottom):
                res.append(matrix[i][right-1])

            right -=1

            if (top < bottom):
                for i in range(right-1  , left-1 , -1):
                    res.append(matrix[bottom-1][i])

                bottom -=1

            if(left <right):
                for i in range(bottom-1, top-1, -1):
                    res.append(matrix[i][left])
                left +=1
        return(res)
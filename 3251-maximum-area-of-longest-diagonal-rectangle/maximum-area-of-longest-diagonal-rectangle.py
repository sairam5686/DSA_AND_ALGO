class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        n = len(dimensions)
        result = 0
        result_diagonal =  0
        for i in range(n):
            length , width = dimensions[i][0] , dimensions[i][1]
            area , diagonal = length * width  , math.sqrt(length **2 + width **2)
            if(result_diagonal < diagonal):
                result_diagonal = max(result_diagonal , diagonal)
                result = area

            if(result_diagonal == diagonal ):
                result = max(area , result)

        return(result)
                
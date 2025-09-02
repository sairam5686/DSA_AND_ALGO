class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], -x[1]))
        result =  0
        for i in range(len(points)):
            upper = points[i][1]
            lower = -float('inf')
            for j in range(i+1 , len(points)):
                current = points[j][1]
                if(current <= upper  and current > lower):
                    result +=1
                    lower = current
                    if(upper == current):
                        break
        return(result)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]: 
        intervals.sort()
        result = []
        for i in (intervals):
            if(len(result) == 0 or  result[-1][-1]< i[0] ):
                result.append(i[:])
            else:
                 result[-1][-1] = max(i[-1] , result[-1][-1])
        return(result)
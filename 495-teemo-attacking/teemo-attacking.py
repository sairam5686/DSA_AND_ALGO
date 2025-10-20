class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = []
        for i in range(len(timeSeries)):
            interval  =  [timeSeries[i] ,  timeSeries[i]+duration]
            if(len(result) == 0  or  result[-1][-1] < interval[0]  ):
                result.append(interval)
            else:
                result[-1][-1] = max(interval[-1] , result[-1][-1])


        total_duration =  0
        for i in result:
            total_duration += (i[1] - i[0])

        return(total_duration)
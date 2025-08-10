class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        points.sort()
        dum_checker = []
        for i in range(0 ,len(points)):
            dum_checker.append((points[i][0]))
        low , high = 0 ,1
        res = 0
        if(len(dum_checker)>1):
            while(high<len(dum_checker)):
                res = max(res , dum_checker[high]- dum_checker[low])
                low +=1
                high +=1
            return(res)
        else:
            return  0

                
def no_of_bou(arr , day , flowers):
    total_counter = 0
    no_of_bb = 0
    max_total_counter = 0
    for i in arr:
        if(day>=i):
            total_counter +=1
        else:
            no_of_bb +=(total_counter//flowers)
            total_counter = 0

    no_of_bb +=(total_counter//flowers)
    return no_of_bb

class Solution(object):
    def minDays(self, bloomDay, m, k):
        low , high = 0 ,max(bloomDay)
        result = -1
        while(low<=high):
            mid = (low+ high)//2
            bouquet = no_of_bou(bloomDay , mid , k)
            if(bouquet>=m):
                result = mid
                high = mid -1
            else:
                low = mid + 1
        return(result)
                
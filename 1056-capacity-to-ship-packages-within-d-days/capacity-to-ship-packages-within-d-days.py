def no_of_days(weight , capacity):
    total_days = 0
    total_capacity =  0
    low = 0
    while(low<len(weight)):
        total_capacity +=weight[low]
        if(total_capacity == capacity):

            total_days +=1
            total_capacity = 0
        elif(total_capacity >capacity ):

            total_days +=1
            total_capacity = weight[low]
        low +=1
    if(total_capacity != 0 ):
        total_days +=1

    return total_days



class Solution(object):
    def shipWithinDays(self, weights, days):
        low , high = max(weights) , sum(weights)
        result = -1
        while(low<=high):
            mid =( low + high )//2
            resu = no_of_days(weights , mid)
            if(resu<=days):
                result = mid
                high = mid -1
            else:
                low =  mid + 1
        return (result)
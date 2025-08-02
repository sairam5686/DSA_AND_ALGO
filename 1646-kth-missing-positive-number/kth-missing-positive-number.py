class Solution(object):
    def findKthPositive(self, arr, k):
        counter = 0
        inc_arr = []
        val = 1
        while(counter != k):
            if(val not in arr):
                inc_arr.append(val)
                counter +=1
            val +=1
        return(inc_arr[-1])

                
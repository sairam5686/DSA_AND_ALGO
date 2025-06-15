def unique_sum(arr , index , dummy , result):
    if(index == len(arr)):
        # if(dummy not in result):
        result.append(dummy[:])
        return
    dummy.append(arr[index])
    unique_sum(arr, index+1, dummy, result)
    dummy.pop()
    unique_sum(arr,index+1, dummy, result)

class Solution(object):
    def subsets(self, arr):
        # arr = [1,2,3]
        # arr = sorted(arr)
        res = []
        unique_sum(arr , 0 , [] , res )
        return(res)
                
def comb_sum(arr,target , index , dummy , result):
    if(index == len(arr)):
        if(sum(dummy) == target):
            result.append(dummy[:])
        return
    if(sum(dummy)+arr[index]<=target):
        dummy.append(arr[index])
        comb_sum(arr, target , index , dummy , result )
        dummy.pop()
    comb_sum(arr, target, index+1, dummy, result)



class Solution(object):
    def combinationSum(self,candidates , target):
        res = []
        comb_sum(candidates, target , 0 , [], res)
        return(res)


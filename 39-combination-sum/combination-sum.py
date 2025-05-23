def combination_sum(index , arr , target , dummy , result ):
    if(len(arr) <= index):
        if(sum(dummy) == target):
            result.append(dummy[:])
        return

    if(target-sum(dummy)>=arr[index]):
        dummy.append(arr[index])
        combination_sum(index, arr, target, dummy, result)
        dummy.pop()
    combination_sum(index+1, arr, target, dummy, result)


class Solution(object):
    def combinationSum(self,candidates , target):
        candidates = sorted(candidates)
        
        result = []
        combination_sum(0, candidates , target , [] , result)
        return(result)
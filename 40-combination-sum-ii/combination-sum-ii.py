def unique_comb(arr , target, index , dummy , result):
    if (sum(dummy) == target):
        result.append(dummy[:])
        return
    for i in range(index , len(arr)):
        if (i >index and arr[i-1] == arr[i]):
            continue
        if((sum(dummy)+arr[i])>target):
            break
        dummy.append(arr[i])
        unique_comb(arr, target, i+1, dummy, result)
        dummy.pop()


class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        res = []
        unique_comb(candidates, target , 0 , [] , res )
        return(res)

        
        
                
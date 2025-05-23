def unique_subseq(index , candidates , target , dummy , result):
    if(sum(dummy) == target):
        result.append(dummy[:])
        return

    for i in range(index,len(candidates)):
        if(target-sum(dummy)<candidates[i]):
            break
        if(index<i and candidates[i] == candidates[i-1]):
            continue
        dummy.append(candidates[i])
        unique_subseq(i+1, candidates, target, dummy, result)
        dummy.pop()
class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        result = []
        unique_subseq(0, candidates , target,[],result)
        return(result)
        
        
                
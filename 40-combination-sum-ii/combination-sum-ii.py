def combinationsum(index,arr,dummy,target,result):

    if(sum(dummy) == target):
        result.append(dummy[:])
        return
    for i in range(index,len(arr)):

        if(index<i and arr[i] == arr[i-1]): continue
        if(target-sum(dummy)<arr[i]): break
        dummy.append(arr[i])
        combinationsum(i+1, arr, dummy, target, result)
        dummy.pop()

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)

        result = []
        combinationsum(0 ,candidates ,[] ,target , result )
        return(result)
        
                
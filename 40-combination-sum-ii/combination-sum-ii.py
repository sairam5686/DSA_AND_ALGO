def CombinationSum2(nums , ind , dummy  , target , result  ):
    if(sum(dummy) == target):
        result.append(dummy[:])
        return

    for i in range(ind , len(nums)):
        if(i > ind and nums[i] == nums[i-1]):
            continue
        if(sum(dummy) > target or nums[i] > target ):
            break


        dummy.append(nums[i])
        CombinationSum2(nums, i+1, dummy, target, result )
        dummy.pop()
    

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        CombinationSum2(candidates,  0  , [] ,  target ,  result ,   )
        return(result)
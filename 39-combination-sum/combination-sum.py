def combination_sum(nums , dummy , length ,  result ,target):
    if(length == len(nums)):
        if(sum(dummy) == target ):
            result.append(dummy[:])
        return

    if(sum(dummy) + nums[length] <= target ):
        dummy.append(nums[length])
        combination_sum(nums, dummy, length, result, target)
        dummy.pop()
    combination_sum(nums,dummy, length+1, result, target)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result  =  []
        combination_sum(candidates  , [] , 0 , result , target )
        return(result)
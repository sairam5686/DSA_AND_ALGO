def CombinationSum(nums , target , dummy , res , val ):
    if (len(nums) == val):
        if(sum(dummy) == target):
            res.append(dummy[:])
        return


    if(sum(dummy)+nums[val] <= target):
        dummy.append(nums[val])
        CombinationSum(nums, target, dummy, res, val)
        dummy.pop()
    CombinationSum(nums, target, dummy, res, val+1)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        CombinationSum(candidates , target  , [] , result , 0)
        return (result)
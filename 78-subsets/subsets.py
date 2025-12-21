def subset(nums , dummy , res , val):
    if(val == len(nums)):
        res.append(dummy[:])
        return
    dummy.append(nums[val])
    subset(nums, dummy, res, val+1)
    dummy.pop()
    subset(nums, dummy, res, val+1)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset(nums , [],result , 0  )
        return (result)
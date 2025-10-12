def subset(nums , length , dummy , result ):
    if(length == len(nums)):
        result.append(dummy[:])
        return

    dummy.append(nums[length])
    subset(nums, length+1, dummy, result)
    dummy.pop(-1)
    subset(nums,length+1, dummy, result)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset(nums , 0 , [] , result)
        return(result)
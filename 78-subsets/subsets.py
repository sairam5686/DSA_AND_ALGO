def Subset(nums , dummy , result , val):
    if(len(nums)== val):
        result.append(dummy[:])
        return
    dummy.append(nums[val])
    Subset(nums,dummy , result, val+1)
    dummy.pop()
    Subset(nums,dummy , result, val+1)




class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        dummy  , result , val = []  , [] , 0
        Subset(nums , dummy , result , val)
        return(result)
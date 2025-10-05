def subset(a , length ,dummy ,  result):
    if(len(a) == length):
        if(dummy not in result):
            result.append(dummy)
        return



    dummy.append(a[length])
    subset(a, length+1,dummy[:] , result)
    subset(a, length+1, dummy[:-1], result)

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset(nums , 0  , [], result)
        return(result)
        
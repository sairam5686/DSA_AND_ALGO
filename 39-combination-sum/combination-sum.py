def comb_sum(nums , dummy , res , index ,target):
    if(index == len(nums)):
        if(sum(dummy) == target):
            res.append(dummy[:])
        return
    if(sum(dummy)<=target):
        dummy.append(nums[index])
        comb_sum(nums, dummy, res, index,target)
        dummy.pop()
    comb_sum(nums, dummy, res, index+1,target)



class Solution(object):
    def combinationSum(self,candidates , target):
        res = []
        index = 0
        comb_sum(candidates , [],res , index, target)
        return (res)
                

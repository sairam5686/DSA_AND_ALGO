class Solution(object):
    def check(self, nums):
        res_nums = []
        low  ,high = 0 , 1
        bp_1 = True
        while(high <len(nums)):
            if(nums[low]<=nums[high]):
                bp_1 = True
            else:
                bp_1 = False
                break
            low +=1
            high +=1
        if(bp_1 == True):
            return(True)
        res_nums +=nums[high::]
        res_nums +=nums[:low+1:]

        bp_2 = False
        low , high = 0,1
        while(high<len(nums)):
            if(res_nums[low]<=res_nums[high]):
                bp_2 = True
            else:
                bp_2 = False
                break
            low +=1
            high +=1

        return(bp_2)
                
class Solution(object):
    def checkSubarraySum(self, nums, k):
        flag = False
        checker = defaultdict(int)
        dummy = 0
        for i in range(len(nums)):
            dummy += nums[i]
            if(dummy%k == 0 and (i+1)>=2):
                flag = True
                break
            if((dummy%k) not in checker ):
                checker[dummy%k] += i
            elif( i- checker[dummy%k] >=2):
                flag = True
                break


        return(flag)
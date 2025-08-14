class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum = defaultdict(int)
        prefix_sum[0]= 1
        adders  = 0
        sums = 0
        result = 0
        for i in range( len(nums)):
            adders += nums[i]
            # if(adders == k):
            #     result +=1
            remaining = adders - k
            if(remaining in prefix_sum):
                result += prefix_sum[remaining]
            prefix_sum[adders] +=1

        return(result)
                        
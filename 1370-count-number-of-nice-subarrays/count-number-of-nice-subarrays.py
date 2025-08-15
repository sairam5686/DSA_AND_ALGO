class Solution(object):
    def numberOfSubarrays(self, nums, k):
        for i in range(len(nums)):
            if(nums[i]%2 == 0 ):
                nums[i] = 0
            else:
                nums[i] = 1
        print(nums)

        dummy =  0
        max_len = 0
        counter = defaultdict(int)
        counter[0] =1

        for i in range(len(nums)):
            dummy += nums[i]
            remainder = dummy - k
            if(remainder in counter):
                max_len +=counter[remainder]
            counter[dummy] +=1

        return(max_len)
                
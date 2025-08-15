class Solution(object):
    def maxNonOverlapping(self, nums, target):
        counter = defaultdict(int)
        counter[0] = 1
        result = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]

            if(prefix_sum == target):
                result +=1
                prefix_sum = 0
                counter.clear()
                counter[0] =1
                continue
            remainder = prefix_sum - target

            if(remainder in counter):
                result +=1
                prefix_sum = 0
                counter.clear()
                counter[0] = 1
            else:
                counter[prefix_sum] =1


        return(result)
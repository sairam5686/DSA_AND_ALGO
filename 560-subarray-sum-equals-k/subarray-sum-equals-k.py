class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        counter[0] +=1
        result = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum - k
            if(remainder in counter):
                result += counter[remainder]
            counter[prefix_sum] +=1
        return (result)
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_counter = defaultdict(int)
        prefix_counter[0]  +=1
        prefix_sum , max_subarray = 0,0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remainder = prefix_sum - k
            if(remainder in prefix_counter):
                max_subarray += prefix_counter[remainder]
            prefix_counter[prefix_sum] += 1
        return(max_subarray)
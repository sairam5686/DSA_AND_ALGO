class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = defaultdict(int)
        for  i in range(len(nums)):
            if( target - nums[i] not in mapper):
                mapper[nums[i]] = i
            elif(target - nums[i] in mapper):
                # print(mapper  ,target - nums[i])
                return ([mapper[target - nums[i]] , i])


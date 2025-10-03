class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        abs_val = sum(nums)
        deep_val = 0
        for i in range(len(nums)):
            dums = str(nums[i])
            for i in range(len(dums)):
                deep_val += int(dums[i])

        return(abs_val - deep_val)
                
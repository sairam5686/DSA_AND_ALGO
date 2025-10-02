class Solution:
    def addDigits(self, nums: int) -> int:
        nums = str(nums)
        if(len(nums) == 1):
            return int(nums)
        else:
            while(len(nums) > 1):
                total_nums = 0
                for i in range(len(nums)):
                    total_nums +=int(nums[i])
                nums= str(total_nums)
            return int(nums)
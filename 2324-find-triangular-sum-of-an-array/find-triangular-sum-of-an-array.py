def solver(nums):
    newNum = [-1]*(len(nums)-1)
    for i in range(len(nums)-1):
        newNum[i] = (nums[i] + nums[i+1]) % 10
    return newNum

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while(len(nums) != 1):
            new_num = solver(nums)
            nums = new_num

        return(sum(nums))
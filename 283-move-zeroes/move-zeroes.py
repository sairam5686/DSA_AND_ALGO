class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        val = nums.count(0)
        arr = []
        for i in (nums):
            if(i != 0 ):
                arr.append(i)

        for i in range(len(arr)):
            nums[i] = arr[i]

        for i in range(len(arr) , len(nums)):
            nums[i] = 0
        

        
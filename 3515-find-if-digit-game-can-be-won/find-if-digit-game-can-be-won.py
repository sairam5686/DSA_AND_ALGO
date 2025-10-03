class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit = 0
        double_digit = 0
        for i in range(len(nums)):
            num = str(nums[i])
            if(len(num) == 1):
                single_digit += int(num)
            else:
                double_digit += int(num)

        if(single_digit == double_digit):
            return(False)
        else:
            return(True)
                
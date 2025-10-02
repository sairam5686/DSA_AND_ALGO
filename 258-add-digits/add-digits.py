class Solution:
    def addDigits(self, nums: int) -> int:
        if(nums == 0 ):
            return  0 
        return 1+(nums-1)%9
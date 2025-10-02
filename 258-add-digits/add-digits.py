class Solution:
    def addDigits(self, nums: int) -> int:
        if(nums % 9 == 0 and nums >  0  ):
            return 9
        if(nums == 0 ):
            return 0
        return (nums%9)

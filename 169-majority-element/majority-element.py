class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = 1
        num = nums[0]
        for i in range(1  , len(nums)):
            if(num == nums[i]):
                val +=1
            else:
                if(val <=0 ):
                    num= nums[i]
                    val = 1
                else:
                    val -=1
        return (num)
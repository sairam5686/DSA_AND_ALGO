class Solution:
    def majorityElement(self, nums: List[int]) -> int:
                
        element = nums[0]
        counter = 1
        for i in range(1 , len(nums)):
            if(nums[i] == element):
                counter +=1
            else:
                if(counter <= 0 ):
                    element = nums[i]
                    counter = 1
                else:
                    counter -=1
        return(element)
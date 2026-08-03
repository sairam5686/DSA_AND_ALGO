class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter=  1
        element =  nums[0]
        for i in range(1 , len(nums)):
            if(element != nums[i]):
                counter -=1
                if(counter == 0 ):
                    element = nums[i]
                    counter = 1
            else:
                counter +=1
        return (element)

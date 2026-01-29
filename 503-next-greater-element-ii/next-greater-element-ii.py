class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        result = []
        for i in range(len(nums)):
            result.append(-1)


        for i in range(len(nums)-1 , -1 , -1):
            while(len(stack) != 0 and stack[-1] < nums[i]):
                stack.pop()
            if(len(stack) ==  0 ):
                result[i] =  -1
                stack.append(nums[i])

            if(stack[-1] > nums[i]):
                result[i]  = stack[-1]
                stack.append(nums[i])

        for i in range(len(nums)-1 , -1 , -1):
            # print( result ,  stack  ,i)
            while(len(stack) != 0 and stack[-1] <= nums[i]):
                stack.pop()
            # print(stack)
            if(len(stack) ==  0 ):
                result[i] =  -1
                stack.append(nums[i])

            if(stack[-1] > nums[i]):
                result[i]  = stack[-1]
                stack.append(nums[i])


        return (result)
class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        
        prev_element= [-1] * len(nums)
        next_element =[len(nums)]*len(nums)
        stack  =[]
        MOD = int(1e9 + 7)
        for i in range(len(nums)):
            while (stack and nums[stack[-1]] > nums[i] ):
                stack.pop()

            if(len(stack) != 0 ):
                prev_element[i] = stack[-1]
                stack.append(i)
            elif(len(stack) == 0 ):
                stack.append(i)
                continue
            elif(nums[stack[-1]] < nums[i] ):
                prev_element[i] = stack[-1]
                stack.append(i)

        stack = []

        for i in range(len(nums)-1, -1 , -1):
            while (stack and nums[stack[-1]] >= nums[i]):
                stack.pop()

            if (len(stack) != 0):
                next_element[i] = stack[-1]
                stack.append(i)
            elif(len(stack) == 0):
                stack.append(i)
                continue
            elif (nums[stack[-1]] < nums[i]):
                next_element[i] = stack[-1]
                stack.append(i)

        print(prev_element , next_element)


        total  = 0
        for i in range(len(nums)):
            left = (i - prev_element[i] )
            right  = (next_element[i] - i)
            total += (left * right)*nums[i]

        return(total%MOD)
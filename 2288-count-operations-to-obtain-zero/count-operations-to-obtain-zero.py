def counter_zero(num1  , num2 , counter):
    if(num1 == 0 or num2 ==0):
        return counter
    if(num1 >= num2):
        return counter_zero(num1 - num2 , num2 , counter+1)
    else:
        return counter_zero(num1, num2 - num1, counter+1)



class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        counter = 0
        result = counter_zero(num1 , num2 , counter)
        return(result)
        
def reducer(num  , counter):
    if(num == 0 ):
        return counter

    if(num%2 == 0 ):
        return reducer(num//2 , counter +1)
    else:
        return reducer(num-1 , counter +1)


class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = reducer(num , 0 )
        return(res)

        
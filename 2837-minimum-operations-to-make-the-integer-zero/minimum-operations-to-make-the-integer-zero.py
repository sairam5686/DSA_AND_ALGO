def set_bit(n):
    n = bin(n)
    n = n[2:]
    counter  =  0
    for i in str(n):
        if(i == '1'):
            counter +=1
    return counter


class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for i in range(0 ,  37 ):
            target = num1 - i*(num2)
            if(target < i ):
                break
            setter = set_bit(target)
            if( setter  <= i):
                return(i)
        return -1
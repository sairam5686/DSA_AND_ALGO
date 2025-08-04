# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        low  , high = 0 , n
        while(low<=high):
            mid = (low + high)//2
            low_upper = guess(mid)
            if(low_upper == 0):
                return mid
            elif(low_upper == -1):
                high = mid - 1

            else:
                low = mid+1

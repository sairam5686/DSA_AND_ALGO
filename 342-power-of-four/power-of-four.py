class Solution(object):
    def isPowerOfFour(self, n):
        return n>0 and log(n,4)% 1== 0  
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mm=2**31
        return n>0 and mm%n==0
        
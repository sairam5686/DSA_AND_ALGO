class Solution(object):
    def isPowerOfThree(self, n):
        mx=3**19
        return (n>0 and mx%n==0 )
           
       


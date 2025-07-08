class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = True
        if(x<0):
            flag = False
        x = abs(x)
        rever = 0
        while(x > 0 ):
            rever = rever *10
            rever += x%10
            x = x//10
        if(rever>=(2**31)):
            return(0)
        if(flag == True):
            return(rever)
        else:
            return(rever*-1)
class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        low , high = 0, len(x)-1
        flag = True
        while(low<high):
            if(x[low] == x[high]):
                low +=1
                high -=1
                flag =True
            else:
                return(False)
                break
                
        return flag
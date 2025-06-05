class Solution(object):
    def isPalindrome(self, s):       
        dummy = ""
        for i in s:
            if(i.isalnum()):
                dummy  = dummy +i
        dummy = dummy.lower()
        if(len(dummy) == 0 or len(dummy) == 1):
            return True
        low , high = 0 , len(dummy)-1
        flag = False
        while(low<high):
            if(dummy[low] == dummy[high]):
                flag = True
                low +=1
                high -=1
            else:
                return False
        return flag

        
class Solution(object):
    def isPalindrome(self, s):
        s =  s.lower().strip()
        ckecher = ""
        for i in range(len(s)):
            if(s[i].isalnum()):
                ckecher +=s[i]
        if(ckecher == ckecher[::-1]):
            return(True)
        else:
            return(False)
                
                
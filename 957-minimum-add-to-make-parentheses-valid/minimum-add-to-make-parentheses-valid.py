class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ranger = 0
        extras = 0
        for i in  s:
            if( i == '('):
                ranger +=1
            elif( i == ')'):
                if(ranger != 0 ):
                    ranger -=1
                else:
                    extras +=1
        return(ranger + extras)
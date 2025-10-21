class Solution:
    def minSwaps(self, s: str) -> int:
        extra_bractets =  0
        max_brackets = 0
        for i in s:
            if(i == "]"):
                extra_bractets +=1
            else:
                extra_bractets -=1
            max_brackets = max(max_brackets , extra_bractets)


        return(((max_brackets+1)//2))
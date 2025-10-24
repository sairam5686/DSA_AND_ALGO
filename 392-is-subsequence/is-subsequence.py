class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        arr = []
        ptr1 , ptr2  = 0  ,0 
        while(ptr2 < len(t) and ptr1 <len(s)):
            if(s[ptr1] == t[ptr2]):
                arr.append(True)
                ptr2 +=1
                ptr1+=1
            else:
                ptr2 +=1

        if(len(arr) == len(s)):
            return True
        else:
            return False
def PalindromePartition(s, dums  , dummy , result , start ):
    if(start == len(s)):
        result.append(dummy[:])
        return
    for i in range(start , len(s)):
        dums = s[start : i+1]
        if(dums[::-1] != dums):
            continue
        dummy.append(dums)
        dums=""
        PalindromePartition(s, dums, dummy, result, i+1)
        dummy.pop()

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = [ ]
        start =  0
        PalindromePartition(s, "" , [] , result , start   )
        return(result)
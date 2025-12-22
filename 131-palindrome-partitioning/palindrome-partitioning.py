def PalindromePartition(s, dums  , dummy , result , start ):
    if(start == len(s)):
        result.append(dummy[:])
        return

    for i in range( start , len(s)):
        # print(s[start : i+1] , dummy  , start , i+1)
        dums  = s[start : i+1]
        dums_len = len(dums)
        if(dums != dums[::-1]):
            continue

        dummy.append(dums)
        dums = ""
        PalindromePartition(s, dums, dummy, result, start+dums_len)
        dummy.pop()


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = [ ]
        start =  0
        PalindromePartition(s, "" , [] , result , start   )
        return(result)

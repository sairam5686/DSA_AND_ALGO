class Solution:
    def maxDepth(self, s: str) -> int:
        stacker = []
        bracker , max_len = 0,0
        for i in range(len(s)):
            if(s[i] == '('):
                stacker.append('(')
                bracker = len(stacker)
            elif(s[i] == ')'):
                stacker.pop()
            max_len = max(max_len , bracker)
        return(max_len)
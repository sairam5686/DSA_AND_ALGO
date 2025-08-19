class Solution(object):
    def numSub(self, s):
        MOD  = 10**9 +7
        ones = 0
        count = 0
        for i in range(len(s)):
            if(s[i] == '1'):
                ones += 1
            else:
                ones = 0
            count += ones
        return((count%MOD))
                
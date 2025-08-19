class Solution(object):
    def longestCommonPrefix(self, strs):
        result =  ""
        if(len(strs) == 0 or len(strs)==1):
            return strs[0]
        for i in range( len(strs[0])):
            for stt in strs:
                if(len(stt) == i or strs[0][i] != stt[i] ):
                    return(result)
            result += strs[0][i]
        return result
class Solution(object):
    def reverseWords(self, s):
        result = ""
        s = s.split()
        result= " ".join(s[::-1])
        return(result)
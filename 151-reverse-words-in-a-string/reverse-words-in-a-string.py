class Solution(object):
    def reverseWords(self, s):
        s.strip()
        arr = s.split(' ')
        print(arr)
        result = ""
        for i in arr[::-1]:
            if (i == ""):
                continue
            result += i + " "

        result = result.strip()
        return(result)
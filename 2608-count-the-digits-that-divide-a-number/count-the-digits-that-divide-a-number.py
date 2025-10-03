class Solution:
    def countDigits(self, num: int) -> int:
        result = 0
        for i in range(len(str(num))):
            str_num = str(num)
            if(num % int(str_num[i]) == 0 ):
                result +=1
        return(result)

                
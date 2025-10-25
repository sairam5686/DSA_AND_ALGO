class Solution:
    def totalMoney(self, n: int) -> int:
        counter = 1
        val = 1
        result = 1
        max_result = 0
        while(n>0 ):
            max_result += result
            if(counter == 7 ):
                result = 0
                counter = 0
                val +=1
                result += val
            else:
                result +=1
            counter +=1
            n-=1

        return(max_result)
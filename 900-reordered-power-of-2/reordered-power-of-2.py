class Solution(object):
    def reorderedPowerOf2(self, n):
        flag = False
        counter = Counter(str(n))
        if(n<=1):
            return True
        for i in range(0 , 30):
            var_counter = Counter(str(2**i))
            if(var_counter == counter):
                flag = True
                break
        return(flag)
def slide_pord(left , right , power):
    MOD = 1000000007
    dummy = 1
    for i in range(left , right+1):
        dummy = (dummy * power[i]) % MOD
    return dummy
class Solution(object):
    def productQueries(self, n, queries):
        bin_n = bin(n)
        bin_n = bin_n[2:]
        # print(bin_n)
        checker = 0
        power_arr =  []
        for i in bin_n[::-1]:
            if(i == '1'):
                power_arr.append((2**(checker)))
            checker +=1

        result = []
        for i in range(len(queries)):
            var_res = slide_pord(queries[i][0] , queries[i][1] , power_arr)
            result.append(var_res)

        return(result)
                
                
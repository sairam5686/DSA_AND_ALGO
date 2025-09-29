def solve(value , i , j , dp):
    if(j-i < 2):
        return 0
    if(dp[i][j] != -1):
        return dp[i][j]
    res = float('inf')
    for k in range(i+1 , j):
        triangle_cost = (value[i]*value[j]*value[k]) + solve(value, i, k, dp) + solve(value, k,j , dp)
        res = min(res , triangle_cost)
    dp[i][j] = res
    return res

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        length = len(values)
        dp = [[-1] *length for _ in range(length)]
        result  = solve (values , 0, length-1  , dp)
        return(result)
                
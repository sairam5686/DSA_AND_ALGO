def Parenthesis(n , dummy , result  , left , right ):
    if(n*2 ==( left + right )):
        if(left == right):
            result.append(dummy)
        return
    Parenthesis(n, dummy+'(', result, left+1, right)
    if(right < left):
        Parenthesis(n, dummy+')', result, left, right+1)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result= []
        dummy = ""
        Parenthesis(n , dummy , result  , 0 , 0 )
        return(result)
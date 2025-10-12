def valid_paranthesis(n ,dummy, right_paran, left_paran ,  result):
    if((n*2) == (left_paran + right_paran)):
        if(right_paran == left_paran):
            result.append(dummy)
        return

    valid_paranthesis(n, dummy+'(', right_paran+1, left_paran, result)
    if(right_paran > left_paran):
        valid_paranthesis(n, dummy+')', right_paran, left_paran+1, result)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        right_paran, left_paran = 0 , 0
        valid_paranthesis(n ,'', right_paran, left_paran ,  result)
        return(result)
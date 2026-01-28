class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        flag = False
        for i in range(len(s)):
            if(len(stack) == 0 and (s[i] == ')' or s[i] == ']' or s[i] == '}'  )):
                return False
         
            elif(s[i] == '(' or s[i] == '[' or s[i] == '{'  ):
                stack.append(s[i])
            elif((stack[len(stack)-1] =="("  and s[i] ==")") or 
                (stack[len(stack)-1] =="["  and s[i] =="]")  or
                (stack[len(stack)-1] =="{"  and s[i] =="}") ):
                stack.pop()
            else:
                return  False
                break
        if(len(stack) != 0 ):
            return (False)
        else:
            return (True)
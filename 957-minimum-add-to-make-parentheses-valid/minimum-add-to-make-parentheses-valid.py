class Solution:
    def minAddToMakeValid(self, s: str) -> int:
    
        stack =  []
        for i in (s):
            print(stack)
            if(i =='(' or (len(stack) == 0 and ')' )):
                stack.append(i)

            elif(stack[-1] == '('  and  i == ')'):
                stack.pop(-1)

            else:
                stack.append(i)
        # print(stack)
        return(len(stack))
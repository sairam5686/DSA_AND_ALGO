class Solution(object):
    def removeOuterParentheses(self, s):
        if(len(s) == 0 or len(s) == 1 or len(s)== 2):
            return("")
        else:
            stack =[]
            ranger = [0]
            for i in range(0, len(s)):
                # print(stack , ranger)
                if(s[i]=="("):
                    stack.append(s[i])
                elif(s[i]==")"):
                    stack.pop()
                if (len(stack) == 0):
                    ranger.append(i+1)

            print(ranger)

            low,high = 0,1
            dummy = ""
            while(high<len(ranger)):
                # print(s[ranger[low]:ranger[high]])
                dummy += s[ranger[low]+1:ranger[high]-1]
                low +=1
                high +=1
            return(dummy)

                
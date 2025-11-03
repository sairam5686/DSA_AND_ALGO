class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:  
        stack = []
        solution = 0
        for i in range(len(colors)):
            if(len(stack) == 0 ):
                stack.append(i)
            elif(colors[stack[-1]]== colors[i]):
                print(stack[-1])
                if(neededTime[stack[-1]] <= neededTime[i]):
                    solution += (neededTime[stack[-1]])
                    stack.pop(-1)
                    stack.append(i)
                else:
                    solution += (neededTime[i])
            else:
                stack.append(i)
        return(solution)
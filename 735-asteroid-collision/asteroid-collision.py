class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i= 0
        while(i < len(asteroids)):
          


            if (not stack ):
                stack.append(asteroids[i])
            elif ((stack[-1] >= 0 and asteroids[i] >= 0) or (stack[-1] < 0 and asteroids[i] < 0) or (stack[-1] < 0 and asteroids[i] >= 0) ):
                stack.append(asteroids[i])
            else:

                while (i < len(asteroids) and  len(stack) != 0 and (stack[-1] >= 0 and  asteroids[i] < 0 )):
                    if (abs(asteroids[i]) == stack[-1]):
                        stack.pop()
                        i += 1
                    elif (abs(asteroids[i]) > stack[-1]):
                        stack.pop()
                    else:
                        break

                    if(not stack and i< len(asteroids)):
                        stack.append(asteroids[i])
                    elif (i< len(asteroids) and ((stack[-1] >= 0 and asteroids[i] >= 0) or (stack[-1] < 0 and asteroids[i] < 0) or (
                            stack[-1] < 0 and asteroids[i] >= 0))):
                        stack.append(asteroids[i])

            i+=1
        return stack
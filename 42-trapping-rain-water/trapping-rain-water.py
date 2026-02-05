
class Solution:
    def trap(self, height: List[int]) -> int:
        
        premax , sufxmax = [0]*len(height),[0]*len(height)


        max_sum = height[0]
        for i in range(len(height)):
            max_sum = max(height[i] , max_sum)
            premax[i] = (max_sum)

        max_sum = height[len(height)-1]
        for i in range(-1 , -len(height)-1 , -1):
            max_sum = max(max_sum , height[i])
            sufxmax[i] = (  max_sum)

        result = 0
        for i in  range(len(height)):
            result += min(premax[i] , sufxmax[i]) - height[i]
        return(result)

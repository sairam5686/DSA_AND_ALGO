class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right =0,len(height)-1
        water = 0
        max_water = 0
        while(left<right):
            if(height[left]<height[right] or height[left]==height[right]):
                water =abs((height[left])*((left+1)-(right+1)))
                left +=1
            elif(height[left]>height[right]):
                water = abs((height[right]) * ((left + 1) - (right + 1)))
                right -=1
            if(water>max_water):
                max_water = water
                
        return(max_water)

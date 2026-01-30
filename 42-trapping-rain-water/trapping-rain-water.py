
class Solution:
    def trap(self, height: List[int]) -> int:
        total , leftmax, rightmax , left = 0 ,0,0 , 0
        right = len(height)-1
        while(left < right):
            if(height[left] <= height[right]):
                if(height[left] < leftmax ):
                    total += leftmax - height[left]
                else:
                    leftmax = height[left]
                left +=1
            else:
                if (height[right] < rightmax):
                    total += rightmax - height[right]
                else:
                    rightmax = height[right]
                right -= 1
        return (total)
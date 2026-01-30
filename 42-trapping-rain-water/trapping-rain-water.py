
class Solution:
    def trap(self, height: List[int]) -> int:
        prefixsum  , suffixsum = [0]*len(height)  , [0]*len(height)
        total , max_element  = 0 , 0
        for i in range(len(height)):
            if(i==0 ):
                max_element = height[i]
                prefixsum[i] = (height[i])
            else:
                max_element = max(max_element , height[i])
                prefixsum[i]=(max_element)

        max_element = 0
        for i in range(len(height)-1 , -1 , -1):
            if(i==len(height)-1 ):
                max_element = height[i]
                suffixsum[i] =  height[i]
            else:
                max_element = max(max_element , height[i])
                suffixsum[i] = (max_element)



        for i in range(len(height)):
       
            if(height[i] < prefixsum[i] and height[i]<suffixsum[i]):
                total += (min(prefixsum[i] , suffixsum[i]) - height[i])
        return (total)
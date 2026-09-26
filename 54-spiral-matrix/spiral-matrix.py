class Solution:
    def spiralOrder(self, nums: list[list[int]]) -> list[int]:
        res = []
        top , down , left , right =  0 ,len(nums)-1 , 0 , len(nums[0])-1
        while(top <= down and left <=right):
            for i in range(left , right+1):
                res.append(nums[top][i])
            top+=1

            for i in range(top , down+1):
                res.append(nums[i][right])

            right -=1

            if (top <=down):
                for i in range(right , left-1 ,-1):
                    res.append(nums[down][i])

                down-=1

            if(left <=right):
                for i in range(down, top-1 , -1):
                    res.append(nums[i][left])
                left +=1
        return(res)

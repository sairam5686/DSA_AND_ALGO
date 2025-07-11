def reverse(arr , start , end ):
    while(start<=end):
        arr[start] , arr[end] = arr[end] , arr[start]
        start +=1
        end -=1


class Solution(object):
    def nextPermutation(self, nums):
        ind = -1

        for  i in range(len(nums)-2 , -1 , -1):
            if(nums[i] < nums[i+1]):
                ind = i
                break

        if(ind == -1):
            reverse(nums , 0 , len(nums)-1)
        else:
            for i in range(len(nums)-1 , ind-1 , -1):
                if(nums[i]>nums[ind]):
                    nums[i] ,nums[ind] = nums[ind],nums[i]
                    break

            reverse(nums, ind+1 ,len(nums)-1)

            print(nums)
                    
                        
                                
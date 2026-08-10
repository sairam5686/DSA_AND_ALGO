def to_reverse(arr  , low , high):
    while(low <= high ):
        arr[low] , arr[high] = arr[high] , arr[low]
        low +=1
        high -=1
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        peak = -1
        for i in range(len(nums)-2 , -1 , -1 ):
            if(nums[i] < nums[i+1]):
                peak = i
                break
        if(peak == -1):
            to_reverse(nums , 0  , len(nums)-1)
        else:
            for i in range(len(nums)-1 , peak , -1):
                if(nums[i] > nums[peak]):
                    nums[i] , nums[peak] = nums[peak]  , nums[i]
                    break

            to_reverse(nums , peak +1 , len(nums)-1)
        # print(nums)                                                
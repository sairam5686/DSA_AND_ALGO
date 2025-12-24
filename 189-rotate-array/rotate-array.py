def reverser(arr , low  , high ):
    while(low < high):
        arr[low] , arr[high] = arr[high] , arr[low]
        low +=1
        high -=1



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <=1:
            pass
        else: 

            if(k > len(nums)):
                k %= len(nums)
            reverser(nums , 0 , len(nums)-1)
            reverser(nums , 0 , k-1)
            reverser(nums , k , len(nums)-1)
            
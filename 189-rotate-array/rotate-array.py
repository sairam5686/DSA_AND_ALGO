def reverse_rage(arr , low , high):
    while(low < high ):
        arr[high] , arr[low] = arr[low] , arr[high]
        high -=1
        low +=1



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        rotation_comp = k%len(nums)
        reverse_rage(nums , 0 , len(nums)-1)
        reverse_rage(nums , 0 , rotation_comp-1)
        reverse_rage(nums , rotation_comp , len(nums)-1)
        return(nums)



        
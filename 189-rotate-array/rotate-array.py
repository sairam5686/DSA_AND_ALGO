def reverse_arr(arr , low , high):
    while(low<high):
        arr[low] , arr[high] = arr[high] , arr[low]
        low +=1
        high -=1

class Solution(object):
    def rotate(self, nums, k):
        k %=len(nums)
        reverse_arr(nums, 0 ,len(nums)-1)
        reverse_arr(nums , 0, k-1)
        reverse_arr(nums , k,len(nums)-1)
            
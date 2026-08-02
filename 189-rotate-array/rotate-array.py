def to_reverse(arr , start , end):
    while(start < end):
        arr[start ]  , arr[end]  = arr[end] , arr[start]
        end -=1
        start+=1


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        
        to_reverse(nums , 0 , len(nums)-1)
        to_reverse(nums , 0 , k-1)
        to_reverse(nums , k  , len(nums)-1)




        
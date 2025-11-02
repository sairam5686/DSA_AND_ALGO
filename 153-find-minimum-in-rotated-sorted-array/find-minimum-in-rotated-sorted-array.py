class Solution:
    def findMin(self, nums: List[int]) -> int:
        low , high = 0 , len(nums)-1
        solution = 999999999
        while(low<=high):
            mid = (low + high) // 2
            if(nums[mid]<= nums[high]):
                solution = min(solution ,nums[mid] )
                high = mid -1
            else:
                solution =min(solution , nums[mid])
                low =mid + 1
        return(solution)
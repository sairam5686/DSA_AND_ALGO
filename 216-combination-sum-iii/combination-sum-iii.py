def CombinationSum3(nums  , k , n , dummy , current_sum , res , ind):
    if(len(dummy) == k and current_sum == n):
        res.append(dummy[:])
        return

    for i in range(ind ,  len(nums)):
        if(i > ind and nums[i] == nums[i-1]):
            continue
        if(current_sum > n or nums[i] > n):
            break
        dummy.append(nums[i])
        CombinationSum3(nums, k, n, dummy, current_sum+nums[i], res, i+1)
        dummy.pop()


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1,2,3,4,5,6,7,8,9]
        res = [ ]
        CombinationSum3(nums , k , n , [] , 0  , res , 0 )
        return(res)
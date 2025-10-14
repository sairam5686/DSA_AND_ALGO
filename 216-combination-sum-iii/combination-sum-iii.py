def combination_sum(nums, index , length , target , dummy , result ):
    if(len(nums) == index):
        if(sum(dummy) == target and len(dummy) == length):
            result.append(dummy[:])
        return

    dummy.append(nums[index])
    combination_sum(nums, index+1, length, target, dummy, result)
    dummy.pop()
    combination_sum(nums, index+1, length, target, dummy, result)

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr_nums = [1,2,3,4,5,6,7,8,9]
        result = []
        combination_sum(arr_nums , 0 ,  k , n , [] , result)
        return(result)
                
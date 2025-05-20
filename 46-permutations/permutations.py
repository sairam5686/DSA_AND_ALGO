def permutation(nums , dummy , map ,result):
    if(len(dummy) == len(nums)):
        result.append(dummy[:])
        return

    for i in range(len(nums)):
        if(map[i] != 1):
            dummy.append(nums[i])
            map[i] = 1
            permutation(nums, dummy, map, result)
            dummy.pop()
            map[i] = 0

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        map = [0]*len(nums)
        permutation(nums,[],map , result)
        return(result)

        
        
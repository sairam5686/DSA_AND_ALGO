
def subsets(index , arr , dummy , result):
    if(dummy not in result):
        result.append(dummy[:])

    for i in range(index , len(arr)):
        if(arr[i] == arr[i-1] and index<i): continue
        dummy.append(arr[i])
        subsets(i+1, arr, dummy, result)
        dummy.pop()
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        subsets(0,nums,[],result)
        return(result)
            
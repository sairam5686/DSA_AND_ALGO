class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        result = [ ]
        for nums in intervals:
            if(len(result)== 0 or result[-1][-1]< nums[0] ):
                result.append(nums)
            else:
                result[-1][-1] = max(result[-1][-1] ,  nums[-1])
        return (result)
                
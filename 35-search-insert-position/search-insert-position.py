class Solution(object):
    def searchInsert(self, arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low , high = 0 ,len(arr)-1
        while(low <= high):
            mid = (low + high) // 2
            if(arr[mid] >= target):
                high = mid -1
            else:
                low = mid + 1

        return(low)

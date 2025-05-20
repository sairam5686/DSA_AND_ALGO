def subseq(index , arr , dummy , target , result):
    if(len(arr) == index):
        if(sum(dummy) == target):
            result.append(dummy[:])
        return

    if(sum(dummy)>target and target-sum(dummy) <=arr[index]):
        return

    if(sum(dummy)<target):
        dummy.append(arr[index])
        subseq(index,arr , dummy , target , result)
        dummy.pop()
    subseq(index+1, arr, dummy, target, result)


class Solution(object):
    def combinationSum(self, arr, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        subseq(0,arr,[],target,result )
        return(result)
                
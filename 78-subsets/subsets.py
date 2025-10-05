def subset(a , length ,dummy ,  result):
    if(len(a) == length):
        result.append(dummy)
        return


    dummy.append(a[length])
    subset(a, length+1,dummy[:] , result)
    subset(a, length+1, dummy[:-1], result)


class Solution:
    def subsets(self, a: List[int]) -> List[List[int]]:
        result = []
        subset(a , 0  , [], result)
        return(result)
                
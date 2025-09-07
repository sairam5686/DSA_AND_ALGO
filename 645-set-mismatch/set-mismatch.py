from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:  
        counter = Counter(nums)
        result = []
        duplicates , missing = 0 , 0 
 
        for i in range(1 , len(nums)+1):
            if( i in counter and counter[i] == 2):
                duplicates = i
            if(i not in counter):
                missing = i
        return([duplicates , missing])

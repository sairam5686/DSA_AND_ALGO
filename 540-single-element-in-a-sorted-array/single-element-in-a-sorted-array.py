class Solution(object):
    def singleNonDuplicate(self, nums):     
        counter  = Counter(nums)
        print(counter)
        for i in  counter.keys():
            if(counter[i] == 1):
                return(i)
                break
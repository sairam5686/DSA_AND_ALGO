class NumArray(object):
    def __init__(self, nums):
        self.nums = nums 
        self.prefix_sums =  []
        A = 0
        for i in range(len(nums)):
            A +=nums[i]
            self.prefix_sums.append(A)
        print(nums , self.prefix_sums )
        

    def sumRange(self, left, right):
        if(left == 0 ):
            return self.prefix_sums[right]
        elif(left == right):
            return self.nums[right]
        else:
            return (self.prefix_sums[right] -  self.prefix_sums[left-1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = defaultdict(int)
        stack = []
        for i in range(len(nums2)-1 ,-1 ,-1 ):
            while(len(stack) != 0 and stack[-1]<nums2[i] ):
                stack.pop()

            if (len(stack)!= 0 and  stack[-1] > nums2[i]):
                counter[nums2[i]] = stack[-1]
                stack.append(nums2[i])

            if(len(stack) == 0 ):
                stack.append(nums2[i])
                counter[nums2[i]] = -1

        result = []
        for i in range(len(nums1)):
            result.append(counter[nums1[i]])
        return (result)
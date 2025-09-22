class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        # print(counter)
        max_freq = max(counter.values())
        result = 0
        for i in counter:
            if(counter[i] == max_freq):
                result += max_freq
        return(result)
                
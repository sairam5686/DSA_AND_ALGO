class Solution:
    def frequencySort(self, s: str) -> str:
        s = Counter(s)
        nums = s.most_common()
        # print(nums)
        result = ""
        for i in range(len(nums)):
            result += nums[i][0]*nums[i][1]
        return(result)
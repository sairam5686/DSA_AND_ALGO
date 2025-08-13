class Solution(object):
    def subarraySum(self, nums, k):
        mpp = defaultdict(int)
        mpp[0] = 1  # Base case

        preSum = 0
        cnt = 0

        for num in nums:
            preSum += num
            remove = preSum - k
            cnt += mpp[remove]
            mpp[preSum] += 1

        return cnt

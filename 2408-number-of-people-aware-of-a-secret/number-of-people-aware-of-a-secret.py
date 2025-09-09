class Solution:
    def peopleAwareOfSecret(self, N: int, delay: int, forget: int) -> int:
        dp = [0] * (N + 1)
        for i in range(1, forget + 1):
            dp[i] = 1
        for i in range(1, N):
            for j in range(i + delay, min(i + forget - 1, N) + 1):
                dp[j] = (dp[j] + dp[i]) % int(1e9 + 7)
        return dp[N]
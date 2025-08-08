class Solution:
    def soupServings(self, n: int) -> float:
         # Convert 'n' into multiples of 25 ml servings (since serving sizes are multiples of 25)
        # m represents the scaled-down amount of soup
        m = math.ceil(n / 25)

        # Dictionary-based DP table:
        # dp[i][j] will store the probability that soup A becomes empty first
        # given i servings of A and j servings of B (in scaled units)
        dp = {}

        # Helper function to calculate probability using the four serving options
        def get_dp(i, j):
            ans = 0
            # Option 1: Serve 100 ml of A and 0 ml of B (i - 4 units of A, j unchanged)
            ans += dp[max(i - 4, 0)][j]
            # Option 2: Serve 75 ml of A and 25 ml of B
            ans += dp[max(i - 3, 0)][max(j - 1, 0)]
            # Option 3: Serve 50 ml of A and 50 ml of B
            ans += dp[max(i - 2, 0)][max(j - 2, 0)]
            # Option 4: Serve 25 ml of A and 75 ml of B
            ans += dp[max(i - 1, 0)][max(j - 3, 0)]

            # Average probability over the 4 equally likely options
            return ans / 4

        # Base case: If both A and B are empty at the same time, probability is 0.5
        dp[0] = {0: 0.5}

        # Fill DP table
        for k in range(1, m + 1):
            # If A is empty (i=0), probability is 1 (A runs out first)
            dp[0][k] = 1
            # If B is empty (j=0), probability is 0 (B runs out first)
            dp[k] = {0: 0}

            # Fill probabilities for all i,j where max(i,j) = k
            for j in range(1, k + 1):
                dp[j][k] = get_dp(j, k)  # probability for (A=j, B=k)
                dp[k][j] = get_dp(k, j)  # probability for (A=k, B=j)

            # Optimization: If the probability for equal A and B is nearly 1, return early
            if 1 - dp[k][k] < 1e-5:
                return 1

        # Return probability when both soups start with m servings
        return dp[m][m]


        
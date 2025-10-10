class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        maxi = -10**9
        vis = [0] * n

        for i in range(n):
            if vis[i]:
                continue

            j = i
            curr_sum = 0

            while j < n:
                vis[j] = 1
                curr_sum += energy[j]
                curr_sum = max(curr_sum, energy[j])
                j += k

            maxi = max(maxi, curr_sum)

        return maxi
                            
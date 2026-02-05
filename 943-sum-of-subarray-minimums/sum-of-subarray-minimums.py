class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        prev_element = [-1] * n
        next_element = [n] * n
        stack = []

        # Previous Smaller Element (strictly smaller)
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                prev_element[i] = stack[-1]
            stack.append(i)

        stack = []

        # Next Smaller Element (smaller or equal)
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                next_element[i] = stack[-1]
            stack.append(i)

        mod = int(1e9 + 7)
        total = 0
        for i in range(n):
            total += (i - prev_element[i]) * (next_element[i] - i) * arr[i]
        return total % mod

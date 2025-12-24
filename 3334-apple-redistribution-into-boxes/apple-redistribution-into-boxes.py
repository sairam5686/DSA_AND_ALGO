class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        apple_sum = sum(apple)
        res = 0
        for i in range(len(capacity)):
            apple_sum -= capacity[i]
            if(apple_sum <= 0 ):
                res = i
                break
        return(res+1)
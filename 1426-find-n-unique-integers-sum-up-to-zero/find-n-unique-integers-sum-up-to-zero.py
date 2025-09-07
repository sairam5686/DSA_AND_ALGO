class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []

        if(n == 0 ):
            return([])

        if(n%2 == 0):
            left  , right = [] , []
            for i in range(1 , n//2+1):
                left.append(-i)
                right.append(i)
            result = left + right

        else:
            left , right = [ ] , [ ]

            for i in range( 1 , n//2+1):
                right.append(i)
                left.append(-i)

            result.extend(left)
            result.append(0)
            result.extend(right)
        return((result))
                
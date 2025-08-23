class Solution:
    def beautySum(self, s: str) -> int:
        sums = 0
        for i in range(len(s)):
            for j in range( i +1 , len(s)):
                counter = Counter(s[i:j+1])
                sums += (max(counter.values()) - min(counter.values()))
        return(sums)
                
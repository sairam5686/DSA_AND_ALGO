class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        n = len(fruits)
        ps = [0]*(n+1)
        for i in range(n):
            ps[i+1] = ps[i] + fruits[i][1]
        left , right = 0 , 0
        max_cost = 0
        p = [fruit[0] for fruit in fruits]
        for right in range(n):
            cost = p[right]-p[left] + min(abs(startPos - p[left]) , abs(startPos - p[right]))
            while (cost>k and left<right):
                left +=1
                cost = p[right]-p[left] + min(abs(startPos - p[left]) , abs(startPos - p[right]))
            if(cost<=k):
                max_cost = max(max_cost , (ps[right+1] - ps[left]))
        return(max_cost)
                
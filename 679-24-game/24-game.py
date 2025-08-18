class Solution(object):
    def judgePoint24(self, cards):
        def solve(nums):
            difference = 10**-5
            n = len(nums)
            if(n==1):
                return abs(24-nums[0])<difference
            
            for i in range(n):
                for j in range(n):
                    if(i==j):
                        continue
                    a ,b = nums[i] , nums[j]
                    branchs  = [a+b , a-b , b-a , a*b]
                    if(abs(a)>difference):
                        branchs.append(b/a)
                    if(abs(b)>difference):
                        branchs.append(a/b)
                    

                    left  = [nums[k] for k in range(n) if(k!=i and k!= j)]
                    
                    for br in branchs:
                        if(solve(left+[br])):
                            return True
            
            return False
        return solve([float(card) for card in cards])
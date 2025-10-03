class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div_m = 0
        div_m_not = 0

        for i in range(1 , n+1):
            if(i%m != 0 ):
                div_m_not +=i
            else:
                div_m +=i
        return(div_m_not - div_m)
                
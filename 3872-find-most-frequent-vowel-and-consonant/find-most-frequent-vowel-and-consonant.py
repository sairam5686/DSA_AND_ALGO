class Solution(object):
    def maxFreqSum(self, s):
        counter = Counter(s)

        max_vowels  , max_consonents = 0 , 0
        for i in counter.keys():
            if(i == 'a' or i=='e' or i=='i' or i== 'o' or i=='u' ):
                max_vowels = max(counter[i] , max_vowels)
            else:
                max_consonents = max( counter[i], max_consonents)
        return(max_vowels + max_consonents)
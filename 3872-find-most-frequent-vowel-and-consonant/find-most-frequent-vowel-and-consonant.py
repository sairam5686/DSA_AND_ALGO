class Solution(object):
    def maxFreqSum(self, s):
        vowels = defaultdict(int)
        consonents = defaultdict(int)
        for i in s:
            if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' ):
                vowels[i] +=1
            else:
                consonents[i] +=1
   


        max_vowel, max_consonents  = 0 ,  0
        for i in vowels.values():
            max_vowel = max(max_vowel , i)

        for i in consonents.values():
            max_consonents = max(max_consonents , i)

        return(max_vowel + max_consonents)

                
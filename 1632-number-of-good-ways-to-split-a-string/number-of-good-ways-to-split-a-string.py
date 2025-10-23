class Solution:
    def numSplits(self, s: str) -> int:
        result = 0
        left_counter = {}
        right_counter = {}
        for i in range(len(s)):
            if (s[i] not in left_counter):
                left_counter[s[i]] = 0
            left_counter[s[i]] +=1

        for j in range( -1,-len(s) , -1):
            left_counter[s[j]] -=1
            if(left_counter[s[j]] == 0 ):
                del left_counter[s[j]]


            if(s[j] not  in right_counter):
                right_counter[s[j]] = 0
            right_counter[s[j]] +=1
            # print(left_counter , right_counter)
            # print(len(left_counter) , len(right_counter))
            if(len(left_counter) == len(right_counter) ):
                result +=1
        return(result)

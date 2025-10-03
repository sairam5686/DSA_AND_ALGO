class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        character  = ""
        for i in counter.keys():
            if(counter[i] == 1):
                character = i
                break
        if(character == ""):
            return -1
        else:
            for i in range(len(s)):
                if(s[i] == character):
                    return(i)

                
class Solution(object):
    def isValid(self, word):
        vowels , consonents , characters  = 0 ,0,0
        digits = 0
        word = word.lower()
        for i in word:
            if(i.isalnum() == False):
                return(False)
                
            elif(i=='0' or i=='9' or i=='8' or i=='7' or i=='6' or i=='5' or i=='4' or i=='3' or i=='2' or i=='1' ):
                digits +=1
                characters +=1
            elif(i == 'a' or i=='e' or i=='i' or i=='o' or i=='u' ):
                vowels +=1
                characters +=1
            else:
                consonents +=1
                characters +=1


        if(characters>=3 and vowels>=1 and consonents >=1):
            return(True)
        else:
            return(False)


                        
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        counter = Counter( sentence)
        if(len(counter) == 26 ):
            return True
        else:
            return False
                
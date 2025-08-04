class Solution(object):
    def checkIfExist(self, arr):
        result = False
        for i in range(len(arr)):
            for j in range(len(arr)):
                if((arr[i] == 2*arr[j] and i != j) or (arr[j] == 2*arr[i]) and i !=j ):
                     return True
        return False
                    
                
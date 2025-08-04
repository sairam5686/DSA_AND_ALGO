class Solution(object):
    def nextGreatestLetter(self, letters, target):
        tar_ascii = ord(target)
        result = letters[0]
        for i in range(len(letters)):
            if(ord(letters[i])>tar_ascii):
                result = letters[i]
                break
        return(result)
                
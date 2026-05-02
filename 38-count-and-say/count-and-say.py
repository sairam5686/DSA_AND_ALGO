def count_say(n):
    result =""
    val = n[0]
    length = 1
    for i in range( 1, len(n)):
        if(val != n[i]):
            result+=str(length)
            result+=val
            val = n[i]
            length = 1
        else:
            length +=1

    result += str(length)
    result += val
    return result



class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        for i in range(n-1):
            result = count_say(result)

        return(result)
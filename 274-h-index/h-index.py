def possible( citations ,num):
    flag = False
    for i in range(len(citations)):
        if(num<=citations[i] and num<=((len(citations)-i))):
            flag = True
            break
    return flag



class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        h_index =  0
        for i in range( 0 , max(citations)+1):
            if(possible(citations,i)):
                h_index = i

        return(h_index)
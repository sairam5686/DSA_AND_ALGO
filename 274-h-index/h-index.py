

class Solution(object):
    def hIndex(self, citations):
        counting_arr = [0]*(len(citations)+1)
        for i in citations:
            counting_arr[min(len(citations) , i)] +=1
        print(counting_arr)

        h = len(citations)
        h_index_counter = counting_arr[len(citations)]
        while(h_index_counter < h):
            h -= 1
            h_index_counter +=counting_arr[h]
        return(h)
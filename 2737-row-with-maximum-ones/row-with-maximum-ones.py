class Solution:
    def rowAndMaximumOnes(self, arr: List[List[int]]) -> List[int]:
       
        max_ones , index = -1 , -1
        for i in range(len(arr)):
            arr[i].sort()
            low , high = 0 , len(arr[0])-1
            marker = -1
            while(low<=high):
                mid  =( low + high )// 2
                if(arr[i][mid] == 1):
                    marker = mid
                    high = mid - 1
                else:
                    low = mid +1
            print(marker, arr[i])
            if(marker == -1):
                continue
            else:
                length  = len(arr[i]) - marker
                if(max_ones < length):
                    max_ones = max(max_ones  , length)
                    index = i

        if(index == -1 and max_ones==-1):
            return [0, 0]
        return([index, max_ones])

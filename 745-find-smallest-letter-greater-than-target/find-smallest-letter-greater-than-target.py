class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        result = letters[0]
        low , high = 0 , len(letters)-1
        while(low <=high):
            mid = (low + high) //2
            if(target<letters[mid]):
                result = letters[mid]
                high = mid - 1
            else:
                low = mid + 1
        return(result)

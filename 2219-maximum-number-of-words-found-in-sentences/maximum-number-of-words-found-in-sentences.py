class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_val  = 0
        for i in sentences:
            dummy = i.split()
            max_val  = max(max_val , len(dummy))
        return(max_val)

                
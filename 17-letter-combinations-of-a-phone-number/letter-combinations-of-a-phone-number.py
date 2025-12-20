def permutation(digits , res  , dummy, val):
    digits_char = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    if(val == len(digits)):
        res.append(dummy)
        return

    for i in digits_char[digits[val]]:
        permutation(digits, res, dummy+i, val+1)



class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        permutation(digits , res  ,  "" , 0)
        return (res)
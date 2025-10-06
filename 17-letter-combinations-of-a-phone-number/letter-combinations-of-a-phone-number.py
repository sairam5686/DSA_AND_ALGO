def comb_digit(digits  , length  , dummy , result):
    dict_number ={
            1: [], 2: ['a', 'b','c'],3: ['d','e','f'],
            4: ['g','h','i'],5: ['j','k','l'],     6: ['m','n','o'],
            7: ['p','q','r','s'], 8: ['t','u','v'],     9: ['w','x','y','z']
        }
    
    if(digits ==""):
        return []

    if(length == len(digits)):
        result.append(dummy)
        return
    character = digits[length]
    value_arr = (dict_number[int(character)])
    for value in value_arr:
        comb_digit(digits, length+1, dummy+value, result)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        dummy = ""
        comb_digit(digits , 0  , dummy , result)
        return(result)
                
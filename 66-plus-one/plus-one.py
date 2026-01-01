class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        Str_digits = ""
        for i in range(len(digits)):
            Str_digits += str(digits[i])

        Str_digits = str(int(Str_digits ) +1)
        result = []
        for i in range(len(Str_digits)):
            result.append(int(Str_digits[i]))
        return (result)
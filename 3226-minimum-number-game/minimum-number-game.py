class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        bob , alice = [] , []
        while(len(nums) != 0 ):
            # for alice
            first_small  = min(nums)
            nums.remove(first_small)
            alice.append(first_small)
            # for bob
            second_small = min(nums)
            nums.remove(second_small)
            bob.append(second_small)


        ptr = 0
        result = []
        while(ptr < len(alice)):
            result.append(bob[ptr])
            result.append(alice[ptr])
            ptr +=1
        return (result)
                
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        bob_ptr , alice_ptr = 1 , 0
        while(alice_ptr < len(nums) or bob_ptr< len(nums)):
            nums[alice_ptr] , nums[bob_ptr] = nums[bob_ptr] , nums[alice_ptr]
            alice_ptr +=2
            bob_ptr +=2
        return(nums)
                
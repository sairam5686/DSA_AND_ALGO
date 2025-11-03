def maker(nums , flower_bb , day ):
    flower = 0
    bb = 0
    for i in range(len(nums)):
        if(day >= nums[i]):

            flower +=1
            if(flower == flower_bb ):

                bb +=1
                flower = 0
        else:
            flower = 0

    return bb

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
  
        solution = -1
        low , high = 1  , max(bloomDay)
        while(low <= high):
            mid =(low + high )//2
            bouquet = maker(bloomDay , k , mid )
            if(bouquet >= m):
                solution = mid
                high = mid -1
            else:
                low  = mid + 1
        return(solution)

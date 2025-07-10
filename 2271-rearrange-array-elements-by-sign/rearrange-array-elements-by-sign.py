class Solution(object):
    def rearrangeArray(self, nums):
        positive , negative = [] , []
        for i in nums:
            if(i >= 0):
                positive.append(i)
            else:
                negative.append(i)

      


        res_pt , pos_pt , neg_pt = 0,0,0

        while(res_pt<len(nums)):
         
            if(res_pt %2 == 0):
                nums[res_pt] =positive[pos_pt]
                res_pt +=1
                pos_pt +=1
            else:
                nums[res_pt] = negative[neg_pt]
                res_pt +=1
                neg_pt +=1

        return(nums)
                        
                        
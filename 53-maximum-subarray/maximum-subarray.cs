public class Solution {
    public int MaxSubArray(int[] nums) {
			int MaxSum = nums.Max();
		int dummy = 0;
			
			for (int i = 0; i < nums.Length; i++)
			{
				dummy += nums[i];
				if (dummy >= 0)
				{
					MaxSum = Math.Max(MaxSum, dummy);
				}
				else
				{
					dummy = 0;
				}

                // MaxSum = Math.Max(MaxSum, dummy);

			}
			
			return(MaxSum);


        
    }
}
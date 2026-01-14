public class Solution {
    public void MoveZeroes(int[] nums) {

        List<int> dummy = new List<int>();
			int zerocounter = 0;
			foreach (int iter in nums)
			{
				if (iter == 0)
				{
					zerocounter++;
				}
				else
				{
					dummy.Add(iter);
				}
			}

			for (int i = 0; i < zerocounter; i++)
			{
				dummy.Add(0);
			}


			for (int i = 0; i < nums.Length; i++)
			{
				nums[i] = dummy[i];
				
			}

		

        
    }
}
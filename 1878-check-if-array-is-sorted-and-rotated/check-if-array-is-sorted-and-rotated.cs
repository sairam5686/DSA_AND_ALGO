public class Solution {
    public bool Check(int[] nums) {
        int low = 0;
			int high = 1;
			while (high < nums.Length)
			{
				if (nums[low] > nums[high])
				{
					break;
				}
                low++;
                high++;
			}

			if (high == nums.Length)
			{
				return(true);
			}


			List<int> checker = new List<int>();

			for (int i = high; i < nums.Length; i++)
			{
				checker.Add(nums[i]);
			}

			for (int i = 0; i < low + 1; i++)
			{
				checker.Add(nums[i]);
			}

			bool flag = false;
			for (int i = 1; i < checker.Count; i++)
			{
				if (checker[i - 1] > checker[i])
				{
					return (false);
				}
				else
				{
					flag = true;
				}
			}
			
			return (flag);
			
			


        
    }
}
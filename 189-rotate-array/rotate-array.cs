public class Solution {
    public void Rotate(int[] nums, int k) {
       	int rotation = k % nums.Length;
			List<int> Result = new List<int>();
			if (rotation == 0)
			{
				Console.Write(nums);
			}
			else
			{

				for (int i = (nums.Length - rotation); i < nums.Length; i++)
				{
					Result.Add(nums[i]);
					
				}

				for (int i = 0; i < (nums.Length - rotation) ; i++)
				{
					Result.Add(nums[i]);
				}


				for (int i = 0; i < nums.Length; i++)
				{
					nums[i] = Result[i];
					// Console.WriteLine(nums[i]);
				
				}
			}




    }
}
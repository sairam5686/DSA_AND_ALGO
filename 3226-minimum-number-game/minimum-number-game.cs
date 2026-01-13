public class Solution {
    public int[] NumberGame(int[] nums) {
        Array.Sort(nums);
			int low  = 0 ;
			int high = 1;
			while (high < nums.Length)
			{
				int temp = nums[low];
				nums[low] = nums[high];
				nums[high] = temp;
				low+=2;
				high+=2;
			}
            return nums;



    }
}
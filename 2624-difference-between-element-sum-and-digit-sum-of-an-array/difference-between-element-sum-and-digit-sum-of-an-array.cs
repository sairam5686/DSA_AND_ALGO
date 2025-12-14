public class Solution {
    public int DifferenceOfSum(int[] nums) {

        int SumDigits = 0;
			int sumAllDigits = 0;
			foreach (var item in nums)
			{
				SumDigits += item;
				var temp = Convert.ToString(item);
				foreach (var i in temp)
				{
					sumAllDigits += i - '0';
				}
				
				
			}
			return(Math.Abs(SumDigits - sumAllDigits));







        
    }
}
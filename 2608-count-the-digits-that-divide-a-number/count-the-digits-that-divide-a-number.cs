public class Solution {
    public int CountDigits(int num) {
        var strDigit = Convert.ToString(num);
			var result = 0;
			for (int i = 0; i < strDigit.Length; i++)
			{
				var temp = strDigit[i] - '0';
				if (num % temp == 0)
				{
					result++;
				}
				
			}
		
			return(result);
        
    }
}
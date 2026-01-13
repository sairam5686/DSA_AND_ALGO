public class Solution {
    public int MaximumWealth(int[][] accounts) {
        int result = 0;
			foreach (var i in accounts)
			{
				if (i.Sum() > result )
				{
					result = i.Sum();
				}
			}

			return (result);

        
    }
}
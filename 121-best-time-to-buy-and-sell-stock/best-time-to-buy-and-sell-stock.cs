public class Solution {
    public int MaxProfit(int[] prices) {
        Stack<int> stack = new Stack<int>();
			int MaxProfit = 0;
			for (int i = prices.Length-1; i >= 0; i--)
			{
				if (stack.Count == 0 || stack.Peek() < prices[i])
				{
					stack.Push(prices[i]);
				}
				else
				{
					int profit = stack.Peek() - prices[i];
					MaxProfit = Math.Max(profit, MaxProfit);
				}
			}
			return (MaxProfit);


    }
}
public class Solution {
    public string FirstPalindrome(string[] words) {
       foreach (var item in words)
			{
				string reversed = string.Concat(item.Reverse());
				if (item == reversed)
				{
					return(item);
				}
			}
			
		return("");

        
    }
}
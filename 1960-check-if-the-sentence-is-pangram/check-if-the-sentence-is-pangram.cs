public class Solution {
    public bool CheckIfPangram(string sentence) {
       
			Dictionary<char, int> counter = new Dictionary<char, int>();
			foreach (var letter in sentence)
			{
				if (counter.ContainsKey(letter))
				{
					counter[letter]++;
				}
				else
				{
					counter[letter] = 1;
				}
			}

			if (counter.Count() == 26)
			{
				return(true);
			}
			else
			{
				return(false);
			}
    }
}
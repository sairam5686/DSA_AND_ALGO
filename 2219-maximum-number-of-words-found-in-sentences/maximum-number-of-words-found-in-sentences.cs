public class Solution {
    public int MostWordsFound(string[] sentences) {
       	int maxval = 0;
			foreach (string iter in sentences)
			{
				int val = iter.Split().Length;
				if (val > maxval)
				{
					maxval = val;
				}
			}
			
			return (maxval);


    }
}
public class Solution {
    public int MostWordsFound(string[] sentences) {
        int result = 0;
			foreach (var item in sentences)
			{
				var splitter = item.Split();
				if (splitter.Length > result)
				{
					result = splitter.Length;
				}

			}
			return(result);
    }
}
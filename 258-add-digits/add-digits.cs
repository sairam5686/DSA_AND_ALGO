public class Solution {
    public int AddDigits(int num) {
 
			int result = 0; 
			
			while (num.ToString().Length != 1)
			{
				string dummy = num.ToString();
				int vari = 0;
				for (int i = 0; i < dummy.Length; i++)
				{
					 vari += int.Parse(dummy[i].ToString());	
				}
				num = vari;
			}
			
			return(num);
		}
    }

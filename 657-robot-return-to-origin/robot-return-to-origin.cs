public class Solution {
    public bool JudgeCircle(string moves) {
        int upDown = 0;
			int RightLeft = 0;
			foreach (var i in moves)
			{
				if (i == 'R')
				{
					RightLeft++;
				}else if (i == 'L')
				{
					RightLeft--;
				}else if (i == 'U')
				{
					upDown++;
				}
				else
				{
					upDown--;
				}
			}


			if (upDown == 0 && RightLeft == 0)
			{
				return (true);
			}
			else
			{
				return (false);
			}
			
    }
}
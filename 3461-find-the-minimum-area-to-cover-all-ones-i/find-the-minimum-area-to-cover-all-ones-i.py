class Solution(object):
    def minimumArea(self, grid):
        row , col =  len(grid) , len(grid[0])
        top , left = row , col
        bottom , right = -1 ,-1

        for i in range((row)):
            for j in range((col)):
                if(grid[i][j]==1):
                    top  = min(top , i)
                    left = min(left , j)
                    bottom = max(bottom , i)
                    right = max(right , j)

        area_row , area_col = (bottom - top)+1 , (right - left)+1
        return area_row*area_col
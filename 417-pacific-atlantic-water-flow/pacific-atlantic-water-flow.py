class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
       
        ROWS , COLS = len(heights) , len(heights[0])
        alt , paci = set( ) , set()
        def  dfs(row , col , visited , prevHeight):
            if((row ,col ) in visited or row == ROWS or col == COLS or row<0 or col < 0 or heights[row][col] <prevHeight ):
                return
        
            visited.add((row , col))
            dfs(row+1, col, visited, heights[row][col])
            dfs(row-1, col, visited, heights[row][col])
            dfs(row, col+1, visited, heights[row][col])
            dfs(row, col-1, visited, heights[row][col])


        for c in range(COLS):
            dfs(0 , c , paci, heights[0][c] )
            dfs(ROWS-1 , c , alt , heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r , 0 , paci , heights[r][0])
            dfs(r , COLS -1 , alt , heights[r][COLS-1])


        result = []
        for i in range(ROWS):
            for j in range(COLS):
                if(i , j) in paci and (i ,j) in alt:
                    result.append([i,j])
        return(result)
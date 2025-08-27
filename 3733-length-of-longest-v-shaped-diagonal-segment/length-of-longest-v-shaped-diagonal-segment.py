class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        directions = [(-1,-1),(-1,1),(1,1),(1,-1)]

        @lru_cache(None)
        def dfs(i,j,target,dir,turn):
            if i<0 or i == m  or j<0 or j == n or grid[i][j] != target: return 0
            target = 0 if target == 2 else 2
            res = 1 + dfs(i+directions[dir][0],j+directions[dir][1],target,dir,turn)
            if not turn:
                newdir = (1 + dir)%4
                res = max(res, 1 + dfs(i+directions[newdir][0],j+directions[newdir][1],target,newdir,not turn))
            return res
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for d in range(4):
                        res = max(res,1 + dfs(i+directions[d][0],j+directions[d][1],2,d,False))
        return res
        
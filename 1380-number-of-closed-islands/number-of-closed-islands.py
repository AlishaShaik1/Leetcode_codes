class Solution:
    def closedIsland(self,grid:list[list[int]])->int:
        m=len(grid)
        n=len(grid[0])

        def dfs(x,y):
            if x<0 or x>=m or y<0 or y>=n or grid[x][y]==1:
                return
            grid[x][y]=1
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

        for x in range(m):
            dfs(x,0)
            dfs(x,n-1)

        for y in range(n):
            dfs(0,y)
            dfs(m-1,y)

        ans=0

        for x in range(1,m-1):
            for y in range(1,n-1):
                if grid[x][y]==0:
                    ans+=1
                    dfs(x,y)

        return ans
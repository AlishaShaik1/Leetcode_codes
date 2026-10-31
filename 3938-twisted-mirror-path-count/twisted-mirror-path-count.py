class Solution:
    def uniquePaths(self,grid:list[list[int]])->int:
        mod=10**9+7
        a=[1]+[0]*(len(grid[0])-1)

        for x in grid:
            b=0
            for y in range(len(x)):
                if x[y]==1:
                    b,a[y]=a[y],b
                else:
                    b=(b+a[y])%mod
                    a[y]=b

        return b
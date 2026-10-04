class Solution:
    def numSquares(self,n:int)->int:
        a=[0]+[n]*n

        for x in range(1,n+1):
            y=1

            while y*y<=x:
                a[x]=min(a[x],a[x-y*y]+1)
                y+=1

        return a[n]
import heapq

class Solution:
    def shortestPath(self,n:int,edges:list[list[int]],labels:str,k:int)->int:
        a=[[] for _ in range(n)]

        for x,y,z in edges:
            a[x].append((y,z))

        b=[[float('inf')]*(k+1) for _ in range(n)]
        b[0][1]=0

        c=[(0,0,1)]

        while c:
            x,y,z=heapq.heappop(c)

            if x!=b[y][z]:
                continue

            if y==n-1:
                return x

            for u,v in a[y]:
                w=z+1 if labels[y]==labels[u] else 1

                if w<=k and x+v<b[u][w]:
                    b[u][w]=x+v
                    heapq.heappush(c,(x+v,u,w))

        return -1
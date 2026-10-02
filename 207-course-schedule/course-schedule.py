class Solution:
    def canFinish(self,numCourses:int,prerequisites:list[list[int]])->bool:
        a=[[] for _ in range(numCourses)]
        b=[0]*numCourses

        for x,y in prerequisites:
            a[y].append(x)
            b[x]+=1

        c=[x for x in range(numCourses) if b[x]==0]
        d=0

        while c:
            x=c.pop()
            d+=1

            for y in a[x]:
                b[y]-=1

                if b[y]==0:
                    c.append(y)

        return d==numCourses
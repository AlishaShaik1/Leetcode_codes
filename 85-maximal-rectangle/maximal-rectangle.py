class Solution:
    def maximalRectangle(self,matrix:list[list[str]])->int:
        if not matrix:
            return 0

        n=len(matrix[0])
        a=[0]*n
        ans=0

        for row in matrix:
            for x in range(n):
                if row[x]=='1':
                    a[x]+=1
                else:
                    a[x]=0

            s=[]
            for x in range(n+1):
                y=a[x] if x<n else 0

                while s and a[s[-1]]>y:
                    h=a[s.pop()]
                    w=x if not s else x-s[-1]-1
                    ans=max(ans,h*w)

                s.append(x)

        return ans
class Solution:
    def nthUglyNumber(self,n:int)->int:
        a=[1]*n
        x=0
        y=0
        z=0

        for i in range(1,n):
            a[i]=min(a[x]*2,a[y]*3,a[z]*5)

            if a[i]==a[x]*2:
                x+=1

            if a[i]==a[y]*3:
                y+=1

            if a[i]==a[z]*5:
                z+=1

        return a[-1]
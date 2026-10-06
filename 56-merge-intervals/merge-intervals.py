class Solution:
    def merge(self,intervals:list[list[int]])->list[list[int]]:
        intervals.sort()
        a=[]

        for x,y in intervals:
            if not a or a[-1][1]<x:
                a.append([x,y])
            else:
                a[-1][1]=max(a[-1][1],y)

        return a
class Solution:
    def countIntersectingIntervals(self,intervals:list[list[int]])->int:
        ans=0
        n=len(intervals)

        for x in range(n):
            for y in range(x+1,n):
                if intervals[x][0]<=intervals[y][1] and intervals[y][0]<=intervals[x][1]:
                    ans+=1

        return ans
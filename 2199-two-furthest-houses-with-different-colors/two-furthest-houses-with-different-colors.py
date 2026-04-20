class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        high=len(colors)-1
        x=0
        for i in range(0,len(colors)):
            if colors[i]!=colors[high]:
                x=max(x,high-i)
            if colors[i]!=colors[0]:
                x=max(x,i-0)
        return x

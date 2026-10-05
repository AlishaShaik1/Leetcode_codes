class Solution:
    def rob(self,nums:list[int])->int:
        x=0
        y=0

        for z in nums:
            x,y=y,max(y,x+z)

        return y
class Solution:
    def minRotations(self,s:str)->int:
        a=0
        x=0

        for y in s:
            y=int(y)
            a+=min(abs(y-x),10-abs(y-x))
            x=y

        return a
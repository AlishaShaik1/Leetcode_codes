class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        x=1
        y=1
        for _ in range(time):
            x+=y

            if x==n:
                y=-1
            elif x==1:
                y=1
        return x
            
        

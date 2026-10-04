class Solution(object):
    def finalPositionOfSnake(self,n,commands):
        ans=0
        for c in commands:
            if c=="RIGHT":ans+=1
            elif c=="LEFT":ans-=1
            elif c=="DOWN":ans+=n
            elif c=="UP":ans-=n
        return ans
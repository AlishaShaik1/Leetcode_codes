class Solution:
    def checkValidString(self,s:str)->bool:
        x=0
        y=0

        for z in s:
            if z=='(':
                x+=1
                y+=1
            elif z==')':
                x-=1
                y-=1
            else:
                x-=1
                y+=1

            if y<0:
                return False

            x=max(x,0)

        return x==0
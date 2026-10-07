class Solution:
    def lastRemaining(self,n:int)->int:
        a=1
        b=1
        c=1

        while n>1:
            if c%2==1 or n%2==1:
                a+=b
            n//=2
            b*=2
            c+=1

        return a
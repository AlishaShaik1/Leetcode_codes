class Solution:
    def countNumbersWithUniqueDigits(self,n:int)->int:
        if n==0:
            return 1

        a=10
        b=9
        c=9

        for x in range(2,min(n,10)+1):
            b*=c
            c-=1
            a+=b

        return a
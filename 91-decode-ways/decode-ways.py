class Solution:
    def numDecodings(self,s:str)->int:
        if not s or s[0]=='0':
            return 0

        a=1
        b=1

        for x in range(1,len(s)):
            c=0

            if s[x]!='0':
                c+=b

            if 10<=int(s[x-1:x+1])<=26:
                c+=a

            a,b=b,c

        return b
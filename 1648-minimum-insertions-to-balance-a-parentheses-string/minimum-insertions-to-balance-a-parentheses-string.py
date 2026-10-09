class Solution:
    def minInsertions(self,s:str)->int:
        a=0
        ans=0
        x=0

        while x<len(s):
            if s[x]=='(':
                a+=1
            else:
                if x+1<len(s) and s[x+1]==')':
                    x+=1
                else:
                    ans+=1

                if a>0:
                    a-=1
                else:
                    ans+=1

            x+=1

        return ans+a*2
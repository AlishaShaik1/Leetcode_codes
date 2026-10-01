class Solution:
    def minWindow(self,s:str,t:str)->str:
        a={}
        b={}

        for x in t:
            a[x]=a.get(x,0)+1

        x=0
        y=0
        z=0
        ans=""

        for y in range(len(s)):
            b[s[y]]=b.get(s[y],0)+1

            if s[y] in a and b[s[y]]<=a[s[y]]:
                z+=1

            while z==len(t):
                if not ans or y-x+1<len(ans):
                    ans=s[x:y+1]

                b[s[x]]-=1

                if s[x] in a and b[s[x]]<a[s[x]]:
                    z-=1

                x+=1

        return ans
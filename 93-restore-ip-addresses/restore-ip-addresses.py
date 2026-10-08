class Solution:
    def restoreIpAddresses(self,s:str)->list[str]:
        ans=[]

        def dfs(x,a):
            if len(a)==4:
                if x==len(s):
                    ans.append('.'.join(a))
                return

            for y in range(x+1,min(x+4,len(s)+1)):
                z=s[x:y]

                if len(z)>1 and z[0]=='0':
                    continue

                if int(z)>255:
                    continue

                a.append(z)
                dfs(y,a)
                a.pop()

        dfs(0,[])
        return ans
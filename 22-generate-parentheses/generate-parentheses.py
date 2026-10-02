class Solution:
    def generateParenthesis(self,n:int)->list[str]:
        a=[]

        def dfs(x,y,z):
            if x==n and y==n:
                a.append(z)
                return

            if x<n:
                dfs(x+1,y,z+'(')

            if y<x:
                dfs(x,y+1,z+')')

        dfs(0,0,'')

        return a
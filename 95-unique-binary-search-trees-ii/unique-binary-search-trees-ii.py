class Solution:
    def generateTrees(self,n:int)->list[Optional[TreeNode]]:
        def dfs(a,b):
            if a>b:
                return [None]

            ans=[]

            for x in range(a,b+1):
                l=dfs(a,x-1)
                r=dfs(x+1,b)

                for y in l:
                    for z in r:
                        q=TreeNode(x)
                        q.left=y
                        q.right=z
                        ans.append(q)

            return ans

        return dfs(1,n)
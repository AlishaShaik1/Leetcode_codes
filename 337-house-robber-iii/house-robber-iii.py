class Solution:
    def rob(self,root:Optional[TreeNode])->int:
        def dfs(x):
            if not x:
                return 0,0

            a,b=dfs(x.left)
            c,d=dfs(x.right)

            return max(a,b)+max(c,d),x.val+a+c

        return max(dfs(root))
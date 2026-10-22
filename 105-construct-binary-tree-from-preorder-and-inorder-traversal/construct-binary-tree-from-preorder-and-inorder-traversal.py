class Solution:
    def buildTree(self,preorder:list[int],inorder:list[int])->Optional[TreeNode]:
        a={x:y for y,x in enumerate(inorder)}
        b=0

        def dfs(l,r):
            nonlocal b
            if l>r:
                return None

            x=preorder[b]
            b+=1
            root=TreeNode(x)
            y=a[x]

            root.left=dfs(l,y-1)
            root.right=dfs(y+1,r)

            return root

        return dfs(0,len(inorder)-1)
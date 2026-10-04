class Solution:
    def buildTree(self,inorder:list[int],postorder:list[int])->Optional[TreeNode]:
        if not inorder:
            return None

        x=postorder.pop()
        a=TreeNode(x)
        y=inorder.index(x)

        a.right=self.buildTree(inorder[y+1:],postorder)
        a.left=self.buildTree(inorder[:y],postorder)

        return a
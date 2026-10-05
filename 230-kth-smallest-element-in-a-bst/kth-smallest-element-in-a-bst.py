class Solution:
    def kthSmallest(self,root:Optional[TreeNode],k:int)->int:
        a=[]
        while True:
            while root:
                a.append(root)
                root=root.left
            root=a.pop()
            k-=1
            if k==0:
                return root.val
            root=root.right
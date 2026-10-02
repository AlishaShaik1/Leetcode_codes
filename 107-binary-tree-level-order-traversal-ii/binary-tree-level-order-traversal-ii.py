class Solution:
    def levelOrderBottom(self,root:Optional[TreeNode])->list[list[int]]:
        if not root:
            return []

        a=[root]
        result=[]

        while a:
            b=[]
            c=[]

            for x in a:
                c.append(x.val)

                if x.left:
                    b.append(x.left)

                if x.right:
                    b.append(x.right)

            result.append(c)
            a=b

        return result[::-1]
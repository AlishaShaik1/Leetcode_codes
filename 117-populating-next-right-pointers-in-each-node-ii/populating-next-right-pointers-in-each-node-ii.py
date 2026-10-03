class Solution:
    def connect(self,root:Optional[Node])->Optional[Node]:
        if not root:
            return root

        a=root

        while a:
            b=Node(0)
            c=b

            while a:
                if a.left:
                    c.next=a.left
                    c=c.next

                if a.right:
                    c.next=a.right
                    c=c.next

                a=a.next

            a=b.next

        return root
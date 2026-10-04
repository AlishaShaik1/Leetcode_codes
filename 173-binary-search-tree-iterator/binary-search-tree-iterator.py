class BSTIterator:

    def __init__(self,root:Optional[TreeNode]):
        self.a=[]
        self.x=root

    def next(self)->int:
        while self.x:
            self.a.append(self.x)
            self.x=self.x.left

        self.x=self.a.pop()
        y=self.x.val
        self.x=self.x.right

        return y

    def hasNext(self)->bool:
        return bool(self.a) or self.x is not None
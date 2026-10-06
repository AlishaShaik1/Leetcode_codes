class Solution:
    def cloneGraph(self,node:Optional['Node'])->Optional['Node']:
        if not node:
            return None

        a={}

        def dfs(x):
            if x in a:
                return a[x]

            a[x]=Node(x.val)

            for y in x.neighbors:
                a[x].neighbors.append(dfs(y))

            return a[x]

        return dfs(node)
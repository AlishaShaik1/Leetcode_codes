class Solution:
    def lexicalOrder(self,n:int)->list[int]:
        a=[]

        def dfs(x):
            if x>n:
                return

            a.append(x)

            for y in range(10):
                z=x*10+y

                if z>n:
                    break

                dfs(z)

        for x in range(1,10):
            dfs(x)

        return a
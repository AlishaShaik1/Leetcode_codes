class Solution:
    def rearrangeArray(self,nums:list[int])->list[int]:
        a=[]
        b={}

        for x in nums:
            b[x]=b.get(x,0)+1

        while b:
            c=sorted(b)

            for x in c:
                a.append(x)
                b[x]-=1

                if b[x]==0:
                    del b[x]

        return a
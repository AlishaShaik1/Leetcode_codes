class Solution:
    def spiralOrder(self,matrix:list[list[int]])->list[int]:
        a=0
        b=len(matrix)-1
        c=0
        d=len(matrix[0])-1
        ans=[]

        while a<=b and c<=d:
            for x in range(c,d+1):
                ans.append(matrix[a][x])
            a+=1

            for x in range(a,b+1):
                ans.append(matrix[x][d])
            d-=1

            if a<=b:
                for x in range(d,c-1,-1):
                    ans.append(matrix[b][x])
                b-=1

            if c<=d:
                for x in range(b,a-1,-1):
                    ans.append(matrix[x][c])
                c+=1

        return ans
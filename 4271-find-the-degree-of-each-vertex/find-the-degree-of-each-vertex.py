class Solution:
    def findDegrees(self,matrix:list[list[int]])->list[int]:
        n=len(matrix)
        a=[0]*n

        for x in range(n):
            for y in range(n):
                if matrix[x][y]==1:
                    a[x]+=1

        return a
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n=len(mat)
        for i in range(4):
            if  mat==target:
                return True
            mat=[[mat[j][n-i-1] for j in range(n)] for i in range(n)]
        return False
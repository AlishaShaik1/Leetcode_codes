class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m,n=len(mat),len(mat[0])
        
        for i in range(m):
            x=k%n
            if i%2==0:
                temp=mat[i][x:]+mat[i][:x]
            else:
                temp=mat[i][-x:]+mat[i][:-x]
            if temp!=mat[i]:
                return False
        return True

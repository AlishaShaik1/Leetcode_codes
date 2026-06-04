class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        for i in range(n):
            row,col=[],[]
            for j in range(n):
                if matrix[i][j] in row:
                    return False
                row.append(matrix[i][j])
                if matrix[j][i] in col:
                    return False
                col.append(matrix[j][i])
        return True
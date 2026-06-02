class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result=[]

        if len(original)!=m*n:
            return []

        for i in range(m):
            row=[]
            for j in range(n):
                row.append(original[i*n +j])
            result.append(row)
        return result

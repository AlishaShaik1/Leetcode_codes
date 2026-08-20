class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        result=[]

        for r in range(rows):
            for c in range(cols):
                distance=abs(r-rCenter)+abs(c-cCenter)
                result.append((distance,r,c))

        result.sort()
        return [[r, c] for distance,r,c in result]
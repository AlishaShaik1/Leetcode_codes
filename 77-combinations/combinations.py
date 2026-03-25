class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        x=[i for i in range(1,n+1)]
        return list(combinations(x,k))

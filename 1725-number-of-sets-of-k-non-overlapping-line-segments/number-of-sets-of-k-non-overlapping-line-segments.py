class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        return comb(n-1+k, 2*k) %int(1e9+7)
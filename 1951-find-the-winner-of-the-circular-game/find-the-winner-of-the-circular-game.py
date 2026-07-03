class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def result(n,k):
            if n==1:
                return 0
            return (result(n-1,k)+k)% n
        return result(n, k) + 1
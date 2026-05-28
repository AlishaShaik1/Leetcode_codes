class Solution:
    def fib(self, n: int) -> int:
        def fibon(n):
            if n==1:
                return 1
            if n==0:
                return 0
            return fibon(n-1)+fibon(n-2)
        return (fibon(n))
class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        elif n<10000:
            return n-999
        elif n<100000:
            return 9000+(n-9999)
        else:
            return 99001
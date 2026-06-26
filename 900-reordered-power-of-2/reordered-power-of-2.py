class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        result=sorted(str(n))

        for i in range(31):
            x=2**i

            if sorted(str(x))==result:
                return True
        return False

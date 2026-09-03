class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        a=float('inf')
        b=float('inf')

        for x in nums1:
            if x%2==0:
                a=min(a,x)
            else:
                b=min(b,x)

        if b==float('inf'):
            return True

        return a>b
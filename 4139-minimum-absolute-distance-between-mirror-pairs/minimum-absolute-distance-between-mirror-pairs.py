class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        result=float('inf')
        x={}

        for i,n in enumerate(nums):
            if n in x:
                result=min(result,i-x[n])
            x[int(str(n)[::-1])]=i
        return result if result!=float('inf') else -1
        
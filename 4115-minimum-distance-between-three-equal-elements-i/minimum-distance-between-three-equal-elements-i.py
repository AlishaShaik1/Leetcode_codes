class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return -1
        result=float('inf')
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    for k in range(j+1,n):
                        if nums[j]==nums[k]:
                            result=min(result,2*(k-i))
        return -1 if result==float('inf') else result
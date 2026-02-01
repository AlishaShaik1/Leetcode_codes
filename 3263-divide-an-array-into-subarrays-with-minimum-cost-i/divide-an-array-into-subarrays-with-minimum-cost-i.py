class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n=len(nums)
        result=float('inf')
        for i in range(1,n):
            for j in range(i+1,n):
                if nums[0]+nums[i]+nums[j]<result:
                    result=nums[0]+nums[i]+nums[j]
        return result
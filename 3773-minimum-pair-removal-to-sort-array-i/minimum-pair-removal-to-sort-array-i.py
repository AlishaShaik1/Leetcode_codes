class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        result=0
        minimum=float('inf')
        x=0
        while nums!=sorted(nums):
            for i in range(len(nums)-1):
                if nums[i]+nums[i+1]<minimum:
                    minimum=nums[i]+nums[i+1]
                    x=i
            nums.pop(x)
            nums[x]=minimum
            minimum,x=float('inf'), 0
            result+=1
        return result
        
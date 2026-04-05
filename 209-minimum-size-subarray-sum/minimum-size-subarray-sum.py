class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j=0
        total=0
        x=float('inf')      
        for i in range(len(nums)):
            total+=nums[i]       
            while total>=target:
                x=min(x,i-j+1)
                total-=nums[j]
                j+=1
        return 0 if x==float('inf') else x
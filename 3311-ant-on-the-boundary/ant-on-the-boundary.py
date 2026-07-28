class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        x=nums[0]
        count=0
        for i in range(1,len(nums)):
            x+=nums[i]
        
            if x==0:
                count+=1
        
        return count
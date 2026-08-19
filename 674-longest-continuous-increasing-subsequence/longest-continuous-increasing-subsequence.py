class Solution:
    def findLengthOfLCIS(self,nums):
        ans=1
        
        curr=1
        for i in range(1,len(nums)):

            if nums[i]>nums[i-1]:
                curr+=1
            else:
                curr=1
            ans=max(ans,curr)
        return ans
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum1=0
        sum2=nums[0]
        for i in range(len(nums)):
            sum1=sum1+nums[i]
            sum2=max(sum2,sum1)
            if sum1<0:
                sum1=0
        return sum2
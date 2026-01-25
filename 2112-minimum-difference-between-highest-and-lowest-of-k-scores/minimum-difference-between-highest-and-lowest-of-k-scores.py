class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k==1:
            return 0
        nums.sort()
        mini=10000000
        for i in range(0,len(nums)-k+1):
            sum1=0
            sum1=nums[i+k-1]-nums[i]
            mini=min(sum1,mini)
        return mini
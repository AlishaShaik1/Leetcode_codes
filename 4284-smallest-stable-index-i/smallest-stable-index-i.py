class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l=0
        r=0
        n=len(nums)
        while r<n:
            m=max(nums[l:r+1])-min(nums[r:n])
            if m<=k:
                return r
            r+=1
        return -1
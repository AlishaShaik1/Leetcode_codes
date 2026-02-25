class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        gap=0
        if n<2:
            return 0
        else:
            for i in range(1, n):
                 gap=max(gap,nums[i]-nums[i-1])

        return gap
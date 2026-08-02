class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1=sum(nums)
        x=0
        y=sum1

        for i in range(len(nums)):
            y-=nums[i]

            if y==x:
                return i
            x+=nums[i]
        return -1
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        result=0
        nums.sort()
        n=len(nums)
        for i in range(0,n):
            if i%2==0:
                result+=nums[i]
        return result
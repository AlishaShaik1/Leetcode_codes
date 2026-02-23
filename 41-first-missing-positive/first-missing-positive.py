class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        x=1
        for num in nums:
            if num==x:
                x=x+1
        return x
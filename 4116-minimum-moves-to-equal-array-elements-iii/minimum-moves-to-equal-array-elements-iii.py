class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n=max(nums)
        count=0
        for x in nums:
            count+=n-x

        return count
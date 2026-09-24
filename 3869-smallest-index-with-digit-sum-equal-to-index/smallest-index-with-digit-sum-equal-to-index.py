class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            x=nums[i]
            r=list(map(int,str(x)))
            result=sum(r)

            if result==i:
                return i
        return -1
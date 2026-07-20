class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        nums=list(num)
        i=len(nums)-1
        while i>=0:
            if nums[i]=='0':
                del nums[i]
                i-=1
            else:
                break
        return "".join(nums)
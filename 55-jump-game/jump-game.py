class Solution:
    def canJump(self, nums: List[int]) -> bool:
        x=0
        for num in nums:
            if x<0:
                return False
            elif num>x:
               x=num
            x-=1
        return True

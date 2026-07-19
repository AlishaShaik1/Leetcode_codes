class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        result=[]
        
        for i in range(len(nums)//2):
            x=min(nums)
            nums.remove(x)

            y=min(nums)
            nums.remove(y)

            result.append(y)
            result.append(x)
        return result
class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        result=[]
        n=len(nums)
        for i in range(n//2):
            x=min(nums)
            y=max(nums)
            nums.remove(x)
            nums.remove(y)

            result.append((x+y)/2)
        return min(result)
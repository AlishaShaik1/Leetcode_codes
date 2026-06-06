class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result=[]
        n=len(nums)
        for i in range(n):
            sum1=sum(nums[:i])
            sum2=sum(nums[i+1:])
            x=abs(sum1-sum2)
            result.append(x)
        return result
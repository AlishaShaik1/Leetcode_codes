class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        x=[]
        y=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        for num in nums:
            if num==0:
                y.append(num)
            else:
                x.append(num)
        return x+y
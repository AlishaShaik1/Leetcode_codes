class Solution:
    def minimumSum(self, num: int) -> int:
        nums=sorted(map(int,str(num)))
        num1=nums[0]*10+nums[2]
        num2=nums[1]*10+nums[3]
        return num1+num2
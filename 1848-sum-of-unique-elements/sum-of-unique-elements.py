class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        x=Counter(nums)
        sum=0
        for num in x:
            if x[num]==1:
                sum+=num
        return sum
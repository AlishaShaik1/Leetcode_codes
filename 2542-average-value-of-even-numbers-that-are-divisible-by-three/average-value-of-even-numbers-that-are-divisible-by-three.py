class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count,result=0,0
        for num in nums:
            if num%6==0:
                count+=1
                result+=num
        if count==0:
            return 0
        return result//count
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left,count,result=0,0,0

        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
            
            while count>k:
                if nums[left]==0:
                    count-=1
                left+=1
            result=max(result,i-left+1)
        return result

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        j=0
        result=[]
        nums.sort()
        for i in range(min(nums),max(nums)):
            if j<len(nums) and i==nums[j]:
                j+=1
            else:
                result.append(i)
        return result
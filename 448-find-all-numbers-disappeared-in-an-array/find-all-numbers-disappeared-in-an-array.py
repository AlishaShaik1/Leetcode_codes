class Solution:
    def findDisappearedNumbers(self, nums): 
        result=[]      
        nums1=set(nums) 
        nums.sort()
        for i in range(1,len(nums)+1):
            if i not in nums1:
                result.append(i)

        return result
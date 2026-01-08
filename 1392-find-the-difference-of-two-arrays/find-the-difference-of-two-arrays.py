class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums3=set(nums1)
        nums4=set(nums2)
        result1=[]
        result2=[]
        for num in nums3:
            if num not in nums4:
                result1.append(num)
        for num in nums4:
            if num not in nums3:
                result2.append(num)
        return [result1,result2]
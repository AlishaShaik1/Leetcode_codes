class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3=[]
        nums1=set(nums1)
        nums1=list(nums1)
        nums2=set(nums2)
        nums2=list(nums2)
        nums1.extend(nums2)
        nums1.sort()
        n=len(nums1)
        for i in range(1,n):
            if nums1[i]==nums1[i-1]:
                nums3.append(nums1[i])
        return nums3


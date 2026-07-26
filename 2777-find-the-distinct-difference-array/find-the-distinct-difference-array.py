class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        sf=[0]*n
        s=set()
        for i in range(n-1,-1,-1):
            sf[i]=len(s)
            s.add(nums[i])
        ans=[]
        s.clear()
        for i in range(n):
            s.add(nums[i])
            ans.append(len(s)-sf[i])
        return ans
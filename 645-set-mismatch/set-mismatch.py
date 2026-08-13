class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        seen=set()
        m=0      
        for x in nums:
            if x in seen:
                m=x
            seen.add(x)
        
        for x in range(1,n+1):
            if x not in seen:
                n=x       
        return [m,n]
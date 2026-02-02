class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        x=[]
        
        for i in range(0,len(nums)):
            if(nums[i]==key):
                x.append(i)
        
        res=[]

        for i in range(0,len(nums)):
            for j in x:
                if(abs(i-j)<=k):
                    res.append(i)
                    break
        
        return res
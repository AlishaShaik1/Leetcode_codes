class Solution:
    def specialArray(self, nums: List[int]) -> int:
        result=[]

        for i in range(len(nums)+1):
            count=0
            for num in nums:
                if i<=num:
                    count+=1
            result.append(count)
            if result[i]==i:
                return i
                
        return -1
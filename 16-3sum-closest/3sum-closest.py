class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest=float('inf')
        
        for i in range(len(nums)-2):
            left,right=i+1,len(nums)-1

            while left<right:
                cur=nums[i]+nums[left]+nums[right]
                if abs(cur-target)<abs(closest-target):
                    closest=cur
                if cur<target:
                    left+=1
                elif cur>target:
                    right-=1
                else:
                    return cur
        
        return closest

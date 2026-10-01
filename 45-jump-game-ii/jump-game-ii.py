class Solution:
    def jump(self,nums:list[int])->int:
        x=0
        y=0
        z=0

        for i in range(len(nums)-1):
            z=max(z,i+nums[i])

            if i==y:
                x+=1
                y=z

        return x
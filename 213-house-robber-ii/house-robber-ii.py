class Solution:
    def rob(self,nums:list[int])->int:
        if len(nums)==1:
            return nums[0]

        def dfs(a):
            x=0
            y=0

            for z in a:
                x,y=y,max(y,x+z)

            return y

        return max(dfs(nums[:-1]),dfs(nums[1:]))
        
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        nums=[]
        
        for i in range(lo,hi+1):
            x=i
            count=0
            while x!=1:
                if x%2==0:
                    x=x//2
                else:
                    x=3*x+1
                count+=1
            nums.append((count,i))
        nums.sort()
        return nums[k-1][1]

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen=set()
        result=-1
        for nums in grid:
            for num in nums:
                if num in seen:
                    result=num
                seen.add(num)
        sum1=sum(seen)
        x=len(grid)*len(grid)
        sum2=x*(x+1)//2
        
        return [result,sum2-sum1]
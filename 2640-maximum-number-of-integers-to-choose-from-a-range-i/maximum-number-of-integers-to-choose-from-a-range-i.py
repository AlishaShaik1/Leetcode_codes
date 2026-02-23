class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_set=set(banned)
        result=[]
        count=0
        for i in range(1,n+1):
            if i not in banned_set and sum(result)+i <=maxSum:
                result.append(i)
                count+=1
                
        return count
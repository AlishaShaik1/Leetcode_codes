class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        result=[]
        for i in  range(len(A)):
            count=0
            for j in range(i+1):
                if A[j] in B[:i+1]:
                    count+=1
            result.append(count)
        return result
                
        return result
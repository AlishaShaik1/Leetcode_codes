class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result=0
        n=len(strs[0])
        for i in range(n):
            for x in range(len(strs)-1):
                if strs[x][i]>strs[x+1][i]:
                    result+=1
                    break
        return result
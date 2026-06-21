class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        x=v[0]
        y=v[-1]
        
        for i in range(min(len(x),len(y))):
            if x[i]!=y[i]:
                return ans
            ans+=x[i]
        return ans

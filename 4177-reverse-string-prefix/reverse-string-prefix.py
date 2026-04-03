class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        x=list(s)
        left,right=0,k-1
        while left<right:
            x[left],x[right]=x[right],x[left]
            left+=1
            right-=1
        return "".join(x)
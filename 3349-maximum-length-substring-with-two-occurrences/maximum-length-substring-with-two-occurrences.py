class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l=0
        m=0
        count={}
        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            while count[s[r]]>2:
                count[s[l]]-=1
                l+=1
            m=max(r-l+1,m)
        return m
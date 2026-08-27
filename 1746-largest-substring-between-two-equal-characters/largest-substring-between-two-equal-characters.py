class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        x={}
        result=-1

        for i in range(len(s)):
            if s[i] in x:
                result=max(result,i-x[s[i]]-1)
            else:
                x[s[i]]=i

        return result
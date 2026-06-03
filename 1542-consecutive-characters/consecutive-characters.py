class Solution:
    def maxPower(self, s: str) -> int:
        result=count=1
        for i in range(len(s)-1):

            if s[i]==s[i+1]:
                count+=1
                result=max(result,count)
            else:
                count=1
        return result
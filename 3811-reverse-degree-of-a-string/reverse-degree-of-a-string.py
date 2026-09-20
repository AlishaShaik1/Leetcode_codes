class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        c=0
        for i in s:
            c+=1
            sum+=c*(123-ord(i))
        return sum
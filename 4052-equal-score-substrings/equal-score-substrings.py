class Solution(object):
    def scoreBalance(self,s):
        total=sum(ord(c)-96 for c in s)
        curr=0
        for i in range(len(s)-1):
            curr+=ord(s[i])-96
            if curr==total-curr:
                return True
        return False
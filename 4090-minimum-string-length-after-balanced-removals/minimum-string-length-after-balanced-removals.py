class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        count1,count2=0,0
        for ch in s:
            if ch == "a":
                count1+=1
            else:
                count2+=1
        return abs(count1-count2)